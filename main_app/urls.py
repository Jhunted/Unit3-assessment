from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.ItemCreate.as_view(), name='add_item'),
  path('<int:pk>/edit/', views.ItemUpdate.as_view(), name='edit_item'),
  path('<int:pk>/delete/', views.ItemDelete.as_view(), name='delete_item'),
]
