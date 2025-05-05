from django.urls import path
from .import views
urlpatterns=[
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('index/',views.index,name="index"),
    path('elements/',views.elements,name="elements"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('login2/',views.login2,name="login2"),
    path('login3/',views.login3,name="login3"),
    path('forgot/',views.forgot,name="forgot"),
    path('forgot2/',views.forgot2,name="forgot2"),
    path('profile/',views.profile,name="profile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('logout/',views.logout,name="logout"),
    ]
