from django.db import models
from django.urls import reverse

class Post(models.Model):
   title = models.CharField(max_length=128)
   body = models.TextField()
   headline = models.TextField()
   image = models.ImageField(default = "default.jpg", upload_to = "Posts-Images")
   slug = models.SlugField(null=False, unique=True)
   
   def __str__(self):
      return self.title

   def get_absolute_url(self):
      return reverse('detail', kwargs={'slug': self.slug})