from django.shortcuts import render
from rest_framework import viewsets

from products.models import Product, Enterprise
from products.serializers import ProductSerializer, EnterpriseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
