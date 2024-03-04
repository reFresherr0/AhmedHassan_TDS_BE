from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Notification
from .serializers import NotificationsSerializer , NotificationsCreateSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status


# Create your views here.

class NotificationListCreateView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['created_at']
    search_fields = ['user_to__username', 'user_from__username']

    def create(self, request, *args, **kwargs):
        serializer = NotificationsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['is_connection_request']:
            serializer.validated_data['message'] = "New connection request"
        notification = serializer.save()
        return Response(NotificationsSerializer(notification).data, status=status.HTTP_201_CREATED)

class NotificationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user_to != self.request.user:
            raise PermissionDenied("You cannot access this notification.")
        return obj

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can update notifications.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can delete notifications.")
        return super().destroy(request, *args, **kwargs)


class NotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Notification.objects.filter(user_to=request.user, is_read=False).count()
        return Response({'unread_count': count})

    def post(self, request):
        Notification.objects.filter(user_to=request.user).update(is_read=True)
        return Response({'message': 'Notifications marked as read'}, status=status.HTTP_200_OK)