from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cat = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Новости'

class Works(models.Model):
    work = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    image = models.FileField(upload_to='work/',null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.work

    class Meta():
        verbose_name = 'Работы'