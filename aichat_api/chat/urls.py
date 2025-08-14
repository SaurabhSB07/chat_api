from django.urls import path
from .views import RegisterView,LoginView,ChatAPIView,TokenBalanceApiView



urlpatterns =[
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('chat_msg/',ChatAPIView.as_view(),name='chat_msg'),
    path('tokenbalance/',TokenBalanceApiView.as_view(),name='tokenbalance')
]