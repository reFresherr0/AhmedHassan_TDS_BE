from django.urls import path
from . import views

urlpatterns = [
    path('',views.NotificationListCreateView.as_view(),name='Notifications-create'),
    path('updateNotifications/<int:id>',views.NotificationRetrieveUpdateDestroyView.as_view(),name='Notifications-retrive-update-destroy'),
    path('count',views.NotificationCountView.as_view(),name='Notifications-count'),
    
]