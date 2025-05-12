from django.urls import path
from .views import home ,SentimentAnalysis
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('sentiment/' , SentimentAnalysis , name='sentiment'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
