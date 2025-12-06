# 📰 DestoNews

🌍 **Live Website:** https://destonews.onrender.com

DestoNews is a modern real-time news web application built using **Django**, allowing users to browse trending headlines from different countries. It includes **user authentication, a clean UI, and smooth navigation**, making it simple and intuitive.

---

## 🚀 Features

- 🔐 User Registration & Login System  
- 📰 Fetch latest news headlines dynamically  
- 🌎 Country-based filtering (India, USA, UK, Canada, Australia, UAE)  
- 📱 Fully responsive UI with Bootstrap  
- ☁️ Live deployment using Render  
- 🎨 Stylish Navbar, animations, and clean design  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | HTML, CSS, Bootstrap |
| Backend | Django |
| Database | SQLite |
| API Used | GNews / Custom configuration |
| Deployment | Render |
| Server | Gunicorn |

---

## 📁 Project Structure

desto-news-master/
│
├── news/ # Main Django app
├── templates/ # HTML templates
├── static/ # CSS & assets
├── manage.py
├── requirements.txt
├── Procfile
└── nlpNewsFeed/ # Project configuration and settings


---

## ⚙️ Installation (Local Setup)

Run the following commands:

```bash
# Clone the project
git clone <your-repo-link>
cd desto-news-master

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver


## ☁️ Deployment (Render)

### 1️⃣ Push code to GitHub

```sh
git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin https://github.com/username/DestoNews.git
git push -u origin main

