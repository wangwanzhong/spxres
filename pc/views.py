from django.shortcuts import render

from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer


def index(request):
    print(request.GET)
    items = Item.objects.all()

    return render(request, 'pc/index.html', {'items': items})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
