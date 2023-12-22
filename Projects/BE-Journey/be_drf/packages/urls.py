from django.urls import path
from . import views


urlpatterns = [
    # path('',views.hello_world,name="packges"),
    path('',views.PackagesApiView.as_view(),name='packages'),
    path('generic',views.PackagesGenericsApiView.as_view(),name='packages2'),
    path('generic/<int:id>',views.PackagesRetrieveUpdateDestroyAPIView.as_view(),name='packages2'),
    
    path('set/', views.PackagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='packages-list'),
    path('set/<int:id>/', views.PackagesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='packages-detail'),
]