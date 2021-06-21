from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.ListCreateAds.as_view()),
    path('ads/<int:pk>', views.RetrievUpdateDeleteAd.as_view()),
]