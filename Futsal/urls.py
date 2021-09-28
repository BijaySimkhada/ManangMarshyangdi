from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHome, name="home"),
    path('register', views.registerUser, name="register"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('about', views.showAbout, name="about"),
    path('book', views.booking, name="book"),
    path('checkbook', views.checkBooking, name="checkbook"),
    path('cancel/<int:id>', views.cancel, name="cancel"),
    path('index/<str:msg>', views.showIndex, name="index")
]
