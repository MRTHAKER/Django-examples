from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class posts(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    text=models.CharField(max_length=1000)
    date=models.DateTimeField(default=timezone.now())
    pub_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pub_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_details",kwargs={"pk":self.pk})

class comment(models.Model):
    author=models.CharField(max_length=200)
    post=models.ForeignKey('blog.posts',related_name='comments',on_delete=models.DO_NOTHING)
    text=models.CharField(max_length=1000)
    date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
