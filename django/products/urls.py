from django.urls import path

from .views import ProductViewSet, UserApi

urlpatterns = [
    path('', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',

    })),
    path('<int:pk>/', ProductViewSet.as_view({
        'put': 'update',
        'get': 'retrieve',
        'delete': 'destroy',
    })),
    path('user/', UserApi.as_view())
]