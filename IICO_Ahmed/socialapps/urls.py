from django.urls import path
from . import views

urlpatterns = [
    path('',views.SocialAppsViews.as_view(),name='Social-apps'),
    path('update',views.SocialAppDetailView.as_view(),name='Social-apps'),
]