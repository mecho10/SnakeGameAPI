from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ScoreSerializer,
    RankingSerializer
)

User = get_user_model()

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class ProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

class ScoreAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_score = serializer.validated_data['score']
        user = request.user
        if new_score > user.high_score:
            user.high_score = new_score
            user.save()
        return Response({'high_score': user.high_score})

class RankingsAPIView(generics.ListAPIView):
    queryset = User.objects.order_by('-high_score')[:10]
    serializer_class = RankingSerializer


# Create your views here.
