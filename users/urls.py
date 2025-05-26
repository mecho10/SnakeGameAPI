from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    ProfileAPIView,
    ScoreAPIView,
    RankingsAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    path('score/', ScoreAPIView.as_view()),
    path('rankings/', RankingsAPIView.as_view()),
]
