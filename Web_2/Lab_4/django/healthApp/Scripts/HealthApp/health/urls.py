from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('list/', views.listt, name="list"),
 
]
  