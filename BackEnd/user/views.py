from django.shortcuts import render
from django.http.response import JsonResponse
from .models import User
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


# Create your views here.

def getAllUsers(request):
    data = User.objects.all()
    response = {
        'All Users' : list(data.values())
    }
    return JsonResponse(response)

@api_view(['GET', 'POST'])
def userData(request):
    if request.method == 'POST':
        print(f"data: {request.data}")
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
