from django.shortcuts import render, get_object_or_404
from .models import News, Works
from django.utils import timezone
from django import forms
# Create your views here.

#   Base Template
def base(request):
    context = {}
    return render(request, 'balay/base.html', context)

#   Index
def index(request):
    new = News.objects.all()[:3]
    works = Works.objects.all()[:4]
    context ={
        'new': new,
        'works': works,
    }
    return render(request, 'balay/index.html', context)

#   Work
def work(request):
    works = Works.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context ={
        'works': works,
    }
    return render(request, 'balay/work.html', context)

#   About
def about(request):
    context ={}
    return render(request, 'balay/about.html', context)

#   Blog
def blog(request):
    new = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    context = {
        'new': new,
    }
    return render(request, 'balay/blog.html', context)

#   Post detail
def post_detail(request, pk):
    new = get_object_or_404(News, pk=pk)

    context ={
        'new': new,
    }
    return render(request, 'balay/detail.html', context)

#   Service
def services(request):
    context ={}
    return render(request, 'balay/services.html', context)

#   Contact
def contact(request):
    context ={}
    return render(request, 'balay/contact.html', context)