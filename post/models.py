from django.db import models

# Create your models here.

class Post(models.Model):
    posttitle = models.TextField()
    shorttext = models.CharField(max_length=144, default="shorttext")
    postbody = models.TextField()
    posttag1 = models.CharField(max_length=100)
    posttag2 = models.CharField(max_length=100)
    posttag3 = models.CharField(max_length=100)
    posttag4 = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails', default=0)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.posttitle
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentauthor = models.CharField(max_length=45)
    commentcontent = models.TextField()
    commentdate = models.DateTimeField(auto_now_add=True)