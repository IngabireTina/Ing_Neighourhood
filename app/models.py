from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hood',default='a.jpg')
    police = models.IntegerField(null=True,blank=True)
    health = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    @classmethod
    def search_hood(cls,search):
    	hoods = cls.objects.filter(name__icontains=search)
    	return hoods
    
    class Meta:
        ordering = ["-pk"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='user_hood',null=True, )

    def __str__(self):
         return self.user.username

    @receiver(post_save, sender=User)
    def save_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def delete_user(self):
        self.delete()


