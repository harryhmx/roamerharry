# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    print('{}: Request Home Page!'.format(request.get_host()))
    return render(request, 'index.html', {'body_title': 'Hello World'})
