from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Notification
from .serializers import NotificationsSerializer , NotificationsCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import UserToPermission


# Create your views here.

class NotificationListCreateView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['user_to__username', 'user_from__username']
    ordering_fields = ['created_at']

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().list(request, *args, **kwargs)
        else:
            queryset = self.get_queryset().filter(user_to=request.user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

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
    permission_classes = [UserToPermission]
    lookup_field='id'


class NotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Notification.objects.filter(user_to=request.user, is_read=False).count()
        return Response({'unread_count': count})

    def post(self, request):
        Notification.objects.filter(user_to=request.user).update(is_read=True)
        return Response({'message': 'Notifications marked as read'}, status=status.HTTP_200_OK)