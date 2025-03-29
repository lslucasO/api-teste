from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/', views.product_api_view, name='api/v1/')
]
