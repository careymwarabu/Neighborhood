from django.db import models
from django.contrib.auth.models import User

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
