from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('<int:pk>/', views.listing_detail, name='listing_detail'),
    path('create_listing/', views.create_listing, name='create_listing'),
]
