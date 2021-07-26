from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    neighborhood_description=models.TextField() 
    occupants_count=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
      
    def save_neighborhood(self):
      self.save()
      
    def delete_neighborhood(self):
      self.delete()  
      
    @classmethod
    def find_neighborhood(cls, name):
      return cls.objects.filter(name_icontains=name) 
    
    @classmethod
    def update_neighborhood(cls, id, name, occupants_count, location):
      update = cls.objects.filter(id=id).update(name=name, occupants_count=occupants_count, location=location)
      return update 

class Profile(models.Model):
  photo=CloudinaryField('image', blank=True)
  bio=models.TextField(max_length=1000, default='No Bio')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

  def save_profile(self):
        self.save()
  def delete_profile(self):
        self.delete()
  @classmethod
  def update_profile(cls, profile_id, bio, photo):
        profile = cls.objects.filter(pk=profile_id).update(bio=bio,photo=photo)
        return profile
  @classmethod
  def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile


class Business(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='business_user',null=True)
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
      return self.name

    def save_business(self):
      self.save()

    def delete_business(self):
      self.delete()
        
    @classmethod
    def find_business(cls, name):
      return cls.objects.filter(name_icontains=name) 
    
    @classmethod
    def update_business(cls, id, name, email):
      update = cls.objects.filter(id=id).update(name=name, email=email)
      return update 

class Post(models.Model):
  title=models.CharField(max_length=100)
  content=models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.title
  def save_post(self):
      self.save()

  def delete_post(self):
      self.delete()
    
  @classmethod
  def update_post(cls, id, title, content):
      update = cls.objects.filter(id=id).update(title=title, content=content)
      return update 