from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    context = {}
    
    #Test context
    context = {'values': [['foo', 32], ['bar', 64], ['baz', 96]]}
    return render_to_response('home/homepage.html', context)