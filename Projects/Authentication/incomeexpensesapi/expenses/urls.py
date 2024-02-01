from django.urls import path
from . import views


urlpatterns = [
    path('', views.ExpenseListCreateAPIView.as_view(), name='expense-list-create'),
    path('<int:id>', views.ExpenseDetailListCreateAPIView.as_view(), name='expense-list-create'),
]