from django.shortcuts import render

from .models import Item


def index(request):
    print(request.GET)
    items = Item.objects.all()

    return render(request, 'pc/index.html', {'items': items})
