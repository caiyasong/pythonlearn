from django.http import JsonResponse
from django.shortcuts import render

# Create your view here.
def index(request):
    return JsonResponse({'data':'ok'})