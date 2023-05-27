from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
        path('hello/', views.HelloWorldView.as_view(), name='hello'),
        path('register/', views.RegisterApiView.as_view(), name='register'),
        path('login/', obtain_auth_token, name='login'),
        path('profile/', views.UserDetailView.as_view(), name='user'),
]
