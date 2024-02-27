from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import SocialApps
from .serializers import SocialAppsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsTdsMember

# Create your views here.

class SocialAppsViews(ListCreateAPIView):
    permission_classes=[IsTdsMember,]
    serializer_class=SocialAppsSerializer
    queryset = SocialApps.objects.all()