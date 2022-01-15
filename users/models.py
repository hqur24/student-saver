from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access = models.CharField(default='1 - Teacher', max_length=100, choices=(('Teacher', '1 - Teacher'), ('Student' ,' 2 - Student' )))
    yeargroup = models.CharField(default='Teacher', max_length=50, choices=(('N/A', 'Teacher'),('Year 12', 'Y12'), ('Year 13' ,' Y13' )))



    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.
