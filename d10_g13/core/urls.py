from django.urls import path
from core import views

urlpatterns = [
    path('index/', views.indexView),
]
