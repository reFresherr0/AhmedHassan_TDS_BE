from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from .models import Package
from .serializer import PackgesSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend








class PackagesApiView(APIView):

    def get (self,request):
        queryset = Package.objects.all() # select * from package;
        serializer= PackgesSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer= PackgesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PackagesGenericsApiView(ListCreateAPIView):
    queryset= Package.objects.all()
    serializer_class= PackgesSerializer
    filter_backends=[DjangoFilterBackend]
    # filterset_fields =['price','is_active','is_over']
    filterset_fields = {
        'price': ['exact','gte', 'lte','gt','lt'],
        'name': ['exact'],
        'is_over': ['exact'],
        } 

    def get_queryset(self):
        return self.queryset.filter()

class PackagesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Package.objects.all()
    serializer_class= PackgesSerializer
    lookup_field='id'


# 
from rest_framework import viewsets

class PackagesViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackgesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'price': ['exact', 'gte', 'lte', 'gt', 'lt'],
        'name': ['exact'],
        'is_over': ['exact'],
    }
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        self.queryset = self.filter_queryset(self.get_queryset()).filter(is_active=True)
        return super().list(self, request, *args, **kwargs)
