from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="aboutUs"),
    path('search/', views.search, name="search"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('borrowed/', views.borrowed, name="borrowed"),
    path('available-books/', views.available, name="available"),
    path('update-books/', views.update, name="update"),
    path('preview/', views.preview, name="preview"),
    path('random/quote/', views.random_quote, name="quote"),

]