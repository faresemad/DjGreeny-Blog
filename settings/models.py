from django.db import models


# Create your models here.
class Company(models.Model):
    # name,logo,call_us,email_us,Subtitle,facebook_link,twitter_link,instagram_link,emails,numbers,address
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/%y/%m/%d/')
    call_us = models.CharField(max_length=100)
    email_us = models.EmailField(max_length=100)
    subtitle = models.TextField(max_length=500)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    emails = models.TextField(max_length=100)
    numbers = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.name