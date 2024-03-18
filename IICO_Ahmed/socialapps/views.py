from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import SocialApps
from .serializers import SocialAppsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsTdsMember, IsAdminCurrentUser
from rest_framework import filters  
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class SocialAppsViews(ListCreateAPIView):
    permission_classes=[IsAdminCurrentUser,]
    serializer_class=SocialAppsSerializer
    queryset = SocialApps.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name',]
    ordering_fields = ['sequence',]
    filterset_fields = ['user_id',]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user_id = self.request.user
    #     if not user_id.is_superuser:
    #         queryset = queryset.filter(user_id=user_id)
    #     return queryset
    
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class SocialAppDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminCurrentUser,]
    serializer_class = SocialAppsSerializer
    queryset = SocialApps.objects.all()
    # lookup_field = 'id'