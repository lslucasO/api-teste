from django.urls import path, include
from django.conf.urls.static import static
from . import views
from backend import settings


urlpatterns = [
    path('api/v1/', views.ProductListView.as_view(), name='products_api_v1')
]

# urlpatterns += static(settings.MEDIA_URL, media_root=settings.MEDIA_ROOT)