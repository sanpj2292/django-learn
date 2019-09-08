from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import PostModel

def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    return HttpResponse('Some Data')