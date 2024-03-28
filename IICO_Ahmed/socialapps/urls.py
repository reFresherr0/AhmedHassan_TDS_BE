from django.urls import path
from . import views

urlpatterns = [
    path('',views.SocialAppsViews.as_view(),name='Social-apps'),
    path('update/<int:id>',views.SocialAppDetailView.as_view(),name='Social-apps'),
]