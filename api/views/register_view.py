# -*- coding: utf-8 -*-
import json

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import User
from api.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = ["/api/token/", "/api/register/", "/api/token/refresh/", "/api/test/"]
    return Response(routes)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == "GET":
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({"response": data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            body = request.body.decode("utf-8")
            data = json.loads(body)
            if "text" not in data:
                return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
            text = data.get("text")
            data = f"Congratulation your API just responded to POST request with text: {text}"
            return Response({"response": data}, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
    return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)


class EditProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    http_method_names = ['put']

class GetProfileView(APIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer

    def get(self, request, pk, format=None):
        user_id = pk  # Get the authenticated user's ID
        user = get_object_or_404(User, pk=user_id)  # Retrieve the authenticated user
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
