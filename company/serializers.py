from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from company.models import Client, Testimony


class ClientSerializer(serializers.ModelSerializer):
    logo = ReadOnlyField(source='get_logo_cropped')

    class Meta:
        model = Client


class TestimonySerializer(TranslatableModelSerializer):
    class Meta:
        model = Testimony