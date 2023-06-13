from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from application.models import Cryptocurrency
from application.serializers import CryptocurrencySerializer


class CryptocurrencyView(ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
