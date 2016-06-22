from .models import Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'usage',
            # 'department',
            'cpu',
            'board',
            'mem',
            'disk',
            'display',
            'up_time',
            'history_usage',
            'description'
        )
