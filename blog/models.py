from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=80, unique=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now )
    date_due = models.DateTimeField(default=timezone.now )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
