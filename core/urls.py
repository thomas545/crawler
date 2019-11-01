from django.urls import path
from . import views




urlpatterns = [
    path('youtube/', views.ListYouTubeVideosView.as_view()),
]
