from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetriveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer