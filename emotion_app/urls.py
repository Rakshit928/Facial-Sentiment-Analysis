from django.urls import path
from . import views

urlpatterns = [
    path('capture/', views.capture, name='capture'),
    path('predict/', views.predict_emotion, name='predict_emotion'),
]