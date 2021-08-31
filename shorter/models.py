from shorter.utils import generate_random_string

from django.db import models
from django.db.models.fields import CharField

import hashlib
import base64
import random
import string

# Create your models here.
class Man(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Url(models.Model):
    origin_url = models.URLField()
    code_url = models.CharField(max_length=5, unique=True)
    
   
    def save(self, *args, **kwargs):
        while True:
            random_str = generate_random_string()
            if not Url.objects.filter(code_url=random_str).exists():
                self.code_url = random_str
                break
            else:
                continue
        super().save(*args, **kwargs)
