from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    blood =  models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    address = models.CharField(max_length=50 )
    phone	= models.CharField(max_length=100, null= True)
    medical = models.CharField(max_length=50, default='Now we are in ')
    rigion = models.CharField(max_length=30 , null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Announcements(models.Model):
    name = models.CharField(max_length=100)
    cell = models.IntegerField()
    b_g  = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class emergency(models.Model):
    b_name = models.CharField(max_length=100)
    cell = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.b_name