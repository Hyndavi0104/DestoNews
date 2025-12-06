import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, "index.html")


# ---------------- NEWS EXTRACTION (Requires Login) ----------------
@login_required(login_url="login")
def extract(request):
    news_data = None
    error = None

    if request.method == "POST":
        country = request.POST.get("country", "in")  # default India

        API_KEY = "54f07b815ef3884f985d1d050de3e7ba"  # Replace with your GNews API key
        url = f"https://gnews.io/api/v4/top-headlines?country={country}&token={API_KEY}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                news_data = response.json().get("articles", [])
            else:
                error = f"API Error: {response.status_code}"
        except Exception as e:
            error = f"Failed to fetch news: {str(e)}"

    return render(request, "extract.html", {"news": news_data, "error": error})


# ---------------- REGISTER ----------------
def register(request):
    if request.user.is_authenticated:
        return redirect("extract")  # logged-in users go straight to news

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


# ---------------- LOGIN ----------------
def user_login(request):
    if request.user.is_authenticated:
        return redirect("extract")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("extract")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


# ---------------- LOGOUT ----------------
@login_required(login_url="login")
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


# ---------------- STATIC PAGES ----------------
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
