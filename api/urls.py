from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/v1/', views.ProductListAPIView.as_view(), name='products_api_v1'),
    path('api/v1/<int:pk>/', views.ProductRetriveAPIView.as_view(), name='products_api_v1'),
]
