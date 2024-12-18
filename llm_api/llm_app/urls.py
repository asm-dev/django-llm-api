from django.urls import path
from .views import GroqAPIView

urlpatterns = [
    path('api/groq/', GroqAPIView.as_view(), name="groq-api")
]