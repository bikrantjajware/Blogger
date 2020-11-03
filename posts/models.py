from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
from django.urls import reverse
import misaka
from  django.utils import  timezone
User = get_user_model()
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',blank=True,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
       # unique_together = ['user','message',]


    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


