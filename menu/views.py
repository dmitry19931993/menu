from django.shortcuts import render

def index(request, pk=None):
    context = {}
    return render(request, 'menu/index.html', context)

def index_pk(request, pk=None):
    context = {"pk": pk}
    return render(request, 'menu/index_pk.html', context)
