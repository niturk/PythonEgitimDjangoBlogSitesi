from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    postlar = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'postlar': postlar})
