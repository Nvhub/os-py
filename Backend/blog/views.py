from django.shortcuts import render
from .models import Article,Category

def home(request):
    context = {'object_list':Article.objects.filter(status='p')}
    return render(request,'home.html',context)