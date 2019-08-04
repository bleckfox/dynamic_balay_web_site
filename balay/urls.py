from django.urls import path, re_path
from . import views


urlpatterns = [
    path('base', views.base, name ='base'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    re_path(r'^$', views.index, name = 'home'),
    re_path(r'^work', views.work, name = 'work'),
    re_path(r'^about', views.about, name = 'about'),
    re_path(r'^blog', views.blog, name = 'blog'),
    re_path(r'^services', views.services, name = 'services'),
    re_path(r'^contact', views.contact, name = 'contact'),

]