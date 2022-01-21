from django.db import models

# Create your models here.

class Text(models.Model):
    text = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.slug 