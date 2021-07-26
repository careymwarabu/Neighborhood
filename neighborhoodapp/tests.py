from django.test import TestCase
from django.contrib.auth.models import User
from .models import Business, Neighborhood, Post, Profile

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Carey', email='carey@gmail.com', password='12345')
      self.neighborhood = Neighborhood(name='Ajanta', location='Bamburi', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.profile = Profile(photo='http:cloudinary/dvnq8iwfs,/profile/carey.jpg', bio='Doing good', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.profile,Profile))  
  def test_save_method(self):
      self.profile.save_profile()     
      profile = Profile.objects.all()
      self.assertTrue(len(profile) > 0) 
  def tearDown(self):
      Profile.objects.all().delete()
  def delete_profile(self):
      self.profile.save_profile()
      profile=Profile.objects.all()
      self.assertEqual(len(profile), 1) 
      self.profile.delete_profile()
      del_profile=Profile.objects.all()
      self.assertEqual(len(del_profile),0)
  def test_update_profile(self):
      self.profile.save_profile()
      self.profile.update_profile(self.profile.id, bio='Feeling good', photo='http:image2')
      update_bio=Profile.objects.get(bio='Feeling good')
      update_profile_photo=Profile.objects.get(photo='http:image2')
      self.assertEqual(update_bio.bio,'Feeling good') 
      self.assertEqual(update_profile_photo.photo,'http:image2') 


class NeighborhoodTestClass(TestCase):
  def setUp(self):
      self.neighborhood = Neighborhood(name='Ajanta', location='bamburi', occupants_count=10)
  def test_instance(self):
      self.assertTrue(isinstance(self.neighborhood,Neighborhood))
  def test_save_method(self):
      self.neighborhood.save_neighborhood()     
      neighborhood = Neighborhood.objects.all()
      self.assertTrue(len(neighborhood) > 0)  
  def tearDown(self):
      Neighborhood.objects.all().delete()
  def delete_neighborhood(self):
      self.neighborhood.save_neighborhood()
      neighborhood=Neighborhood.objects.all()
      self.assertEqual(len(neighborhood), 1) 
      self.neighborhood.delete_neighborhood()
      del_neighborhood=Neighborhood.objects.all()
      self.assertEqual(len(del_neighborhood),0)
  def test_update_neighborhood(self):
      self.neighborhood.save_neighborhood()
      self.neighborhood.update_neighborhood(self.neighborhood.id, name='Tudor', location='poly', occupants_count=9)
      update_name=Neighborhood.objects.get(name='Tudor')
      update_occupant=Neighborhood.objects.get(occupants_count=9)
      self.assertEqual(update_name.name,'Tudor') 
      self.assertEqual(update_occupant.occupants_count,9) 


class BusinessTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Carey', email='carey@gmail.com', password='12345')
      self.neighborhood = Neighborhood(name='Ajanta', location='bamburi', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.business = Business(name='Mwarabu Dishes', description='food center', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.business,Business))  
  def test_save_method(self):
      self.business.save_business()     
      business = Business.objects.all()
      self.assertTrue(len(business) > 0) 
  def tearDown(self):
      Business.objects.all().delete()

  def delete_business(self):
      self.business.save_business()
      business=Business.objects.all()
      self.assertEqual(len(business), 1) 
      self.business.delete_business()
      del_business=Business.objects.all()
      self.assertEqual(len(del_business),0)
  def test_update_business(self):
      self.business.save_business()
      self.business.update_business(self.business.id, name='Mwarabu', email='mwarabud@@gmail.com')
      update_name=Business.objects.get(name='Mwarabu')
      update_email=Business.objects.get(email='mwarabud@gmail.com')
      self.assertEqual(update_name.name,'Mwarabu') 
      self.assertEqual(update_email.email,'mwarabud@gmail.com') 

class PostTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Carey', email='carey@gmail.com', password='12345')
      self.neighborhood = Neighborhood(name='Ajanta', location='bamburi', occupants_count=10)
      self.user.save()
      self.neighborhood.save()
      self.post = Post(title='Roadblock', content='driving test ongoing', user=self.user, neighborhood=self.neighborhood)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.post,Post))  
  def test_save_method(self):
      self.post.save_post()     
      post = Post.objects.all()
      self.assertTrue(len(post) > 0) 
  def tearDown(self):
      Post.objects.all().delete()

  def delete_post(self):
      self.post.save_post()
      post=Post.objects.all()
      self.assertEqual(len(post), 1) 
      self.post.delete_post()
      del_post=Post.objects.all()
      self.assertEqual(len(del_post),0)

  def test_update_post(self):
      self.post.save_post()
      self.post.update_post(self.post.id, title='Concert', content='Concert on the road')
      update_post=Post.objects.get(title='Concert')
      update_content=Post.objects.get(content='Concert on the road')
      self.assertEqual(update_post.title,'Concert') 
      self.assertEqual(update_content.content,'Concert on the road') 
