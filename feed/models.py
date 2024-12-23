from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False) # text cannot be blank and null
    image = ImageField() # image can be blank and null

    def __str__(self):
        return self.text