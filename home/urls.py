from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('search/', views.search, name="search"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handelLogin, name="handelLogin"),
    path('logout/', views.handelLogout, name="handelLogout"),
]