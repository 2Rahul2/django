from django.urls import path
from .views import home ,SentimentAnalysis

urlpatterns = [
    path('', home, name='home'),
    path('sentiment/' , SentimentAnalysis , name='sentiment'),
]
