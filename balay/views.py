from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import News, Works
from .forms import Email
from django.utils import timezone
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
    if request.method == 'POST':
        msg = Email(request.POST)
        if msg.is_valid():
            name = msg.cleaned_data['name']
            email = msg.cleaned_data['email']
            subject = msg.cleaned_data['name', 'subject']
            message = msg.cleaned_data['message']

            sent_to = ['Your_E-mail']

            send_mail(subject, message, email, sent_to)
    else:
        msg = Email()

    context ={
        'msg': msg
    }
    return render(request, 'balay/contact.html', context)