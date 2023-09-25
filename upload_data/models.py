from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Files(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    file_description = models.TextField(null=True,blank=True)
    file_image = models.ImageField(upload_to="images")