from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    
    def __str__(self):
        return self.title