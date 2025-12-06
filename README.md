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



## ⚙️ Installation (Local Setup)

Run the following commands:

#### Clone the project
git clone <your-repo-link>
cd desto-news-master

#### Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

#### Install dependencies
pip install -r requirements.txt

#### Run migrations
python manage.py migrate

#### Run server
python manage.py runserver

---


## ☁️ Deployment (Render)

###  1️⃣ Push code to GitHub

git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin https://github.com/Hyndavi0104/DestoNews.git
git push -u origin main

###  2️⃣ Add Procfile

web: gunicorn nlpNewsFeed.wsgi:application --bind 0.0.0.0:$PORT

### 3️⃣ Create App on Render

Go to Render.com

Click New → Web Service

Select your GitHub repository

Set environment to Python 3.12+

Click Deploy

Render will automatically detect requirements.txt.


### ▶️ Static Files Setup (Before Deploy)

#### Run:

python manage.py collectstatic


#### When prompted:

Type 'yes' to continue:


## 🙌 Credits

Developed by Hyndavi Thota 🎉
Created to learn, explore, and build a functional Django web application.

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...



