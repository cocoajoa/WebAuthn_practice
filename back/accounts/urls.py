# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/begin/', views.RegisterBeginView ),
    path('register/complete/', views.RegisterCompleteView),
    path('login/begin/', views.LoginBeginView),
    path('login/complete/', views.LoginCompleteView),
    path('logout/', views.LogoutView),
]