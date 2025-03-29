from django.urls import path
from .views import HomePageView, TestView, TextbookView, MePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestView.as_view(), name='test'),
    path('textbook/', TextbookView.as_view(), name='textbook'),
    path('me/', MePageView.as_view(), name='me'),
    # other URL patterns...
]