from django.shortcuts import render

# In authentication/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response(UserSerializer(user).data)
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )
