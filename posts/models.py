from django.db import models
from django.conf import Settings
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(Settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title