from django.urls import path
from .views import ChallengeListView

urlpatterns = [
    path('challenge/', ChallengeListView.as_view(), name='challenge-list'),
]
