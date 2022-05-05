# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    print('{}: Request Home Page!'.format(request.get_host()))
    return render(request, 'index.html', {'body_title': 'Hello World'})

def items(request):
    print('{}: Request Archives Page!'.format(request.get_host()))
    return render(request, 'index.html', {'head_title': 'Archives | RoamerHarry', 'body_title': 'Archives'})
