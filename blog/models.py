from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #Defines model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Link to another model?
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #Publish post, set date
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #Return title when printed
        return self.title