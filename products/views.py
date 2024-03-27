from django.shortcuts import render
from rest_framework import viewsets, pagination

from products.models import Product, Enterprise
from products.serializers import ProductSerializer, EnterpriseSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Количество элементов на страницу
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    pagination_class = CustomPagination