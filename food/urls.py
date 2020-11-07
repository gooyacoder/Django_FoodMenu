from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.index, name='index'),
    path('food/<int:item_id>/', views.detail, name='detail'),
    
]