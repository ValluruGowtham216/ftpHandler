from django.urls import path
from .views import FetchFileView

urlpatterns = [
    path('fetch-file/', FetchFileView.as_view(), name='fetch-file'),
]