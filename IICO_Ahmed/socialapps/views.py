from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import SocialApps
from .serializers import SocialAppsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsTdsMember, IsAdminCurrentUser
from rest_framework import filters  
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.

class SocialAppsViews(ListCreateAPIView):
    permission_classes=[IsAuthenticated,]
    serializer_class=SocialAppsSerializer
    queryset = SocialApps.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['sequence',]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(user=user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SocialAppDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminCurrentUser,]
    serializer_class = SocialAppsSerializer
    queryset = SocialApps.objects.all()
    # lookup_field = 'id'