from rest_framework import viewsets
from company.models import Client, Testimony
from company.serializers import ClientSerializer, TestimonySerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.select_related().all()
    serializer_class = ClientSerializer


class TestimonyViewSet(viewsets.ModelViewSet):
    queryset = Testimony.objects.select_related().all()
    serializer_class = TestimonySerializer