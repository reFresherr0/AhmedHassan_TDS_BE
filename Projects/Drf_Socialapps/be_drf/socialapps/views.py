from django.shortcuts import render
from rest_framework import viewsets
from .models import SocialApps
from .serializers import SocialAppsSerializer
# Create your views here.

class SocialAppsViews(viewsets.ModelViewSet):
    serializer_class=SocialAppsSerializer
    queryset = SocialApps.objects.all()

   

