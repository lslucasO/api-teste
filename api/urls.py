from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/', views.ProductListView.as_view(), name='products_api_v1')
]
