from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home
    path('', news_views.home, name='home'),

    # Auth Routes
    path('login/', accounts_views.login_view, name='login'),
    path('register/', accounts_views.register_view, name='register'),
    path('logout/', accounts_views.logout_view, name='logout'),

    # News app
    path('news/', include('news.urls')),
]
