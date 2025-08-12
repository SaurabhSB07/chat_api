from django.urls import path
from .views import UserRegisterationView,UserLoginView

urlpatterns =[
    path('register/',UserRegisterationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login')
]