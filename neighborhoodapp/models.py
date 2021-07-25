from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from django.db import IntegrityError


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length= 60)
    location = models.CharField(max_length=50)
    count = models.IntegerField(null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, name):
        cls.objects.filter(name=name).delete()

    @classmethod
    def find_neighbourhood(cls, search_term):
        search_results = cls.objects.filter(name__icontains = search_term)
        return search_results

    def update_neighbourhood(self,name):
        self.name = name
        self.save()

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    prof_pic = CloudinaryField('image')

    def __str__(self):
        return self.name

class Business(models.Model):
    description = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    
class Post(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image')
    post = HTMLField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
