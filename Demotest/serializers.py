from rest_framework import serializers
from .models import ChallengeModel

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeModel
        fields = ['mission', 'vision', 'objectives']
