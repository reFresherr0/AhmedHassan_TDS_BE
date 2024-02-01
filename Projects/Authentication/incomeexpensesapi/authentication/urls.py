from django.urls import path
from .views import RegisterView, VerifyEmail


urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('email-verify/', VerifyEmail.as_view(), name='Email-Verify'),
]