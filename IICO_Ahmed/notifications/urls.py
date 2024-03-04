from django.urls import path
from . import views

urlpatterns = [
    path('',views.NotificationListCreateView.as_view(),name='Notifications-create'),
    path('',views.NotificationRetrieveUpdateDestroyView.as_view(),name='Notifications-retrive-update-destroy'),
    path('',views.NotificationCountView.as_view(),name='Notifications-count'),
    
]