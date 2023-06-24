from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChallengeModel
from .serializers import ChallengeSerializer

class ChallengeListView(APIView):
    def get(self, request):
        queryset = ChallengeModel.objects.all()
        serializer = ChallengeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChallengeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
