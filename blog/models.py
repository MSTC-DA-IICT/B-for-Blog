from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    subtitle = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to='blog/thumbnails/')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_id')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']

    def get_image(self):
        return self.thumbnail.url

    def __str__(self):
        return self.title

