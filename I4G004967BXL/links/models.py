from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from .managers import ActiveLinkManager

# Create your models here.


class Link(models.Model):
    target = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, null=False)
    objects = models.Manager()
    public = ActiveLinkManager()

    def save(self, *args, **kwargs):
        self.description = slugify(self.target)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.target
