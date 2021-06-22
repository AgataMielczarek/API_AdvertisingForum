from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('ads/', views.ListCreateAds.as_view()),
    path('ads/<int:pk>/', views.RetrieveUpdateDeleteAd.as_view()),
    path('display-industry/<str:pk>/', views.DisplayIndustry.as_view()),
    path('users/', views.ListUsers.as_view()),
    path('create-user/', views.CreateUser.as_view()),
    path('get-token/', obtain_auth_token),
]