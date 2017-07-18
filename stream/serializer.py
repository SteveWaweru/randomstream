from rest_framework import serializers
from models import RandomNumber


class RandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomNumber
        fields = ('number',)