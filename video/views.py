from django.shortcuts import render
import json

# Create your views here.


def gravarVideo(request):

    context = {}
    return render(request, 'video/gravar.html', context)
