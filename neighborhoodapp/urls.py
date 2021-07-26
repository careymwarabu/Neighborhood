from django.urls import path
from . import views


urlpatterns = [
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),  
  path('logout/', views.logoutUser, name="logout"),
  path('', views.home, name='home' ),
  path('dashboard', views.dashboard, name='dashboard' ),
  path('user/<int:user_id>', views.userPage, name='user_page'),
  path('account/', views.accountSettings, name='account'),
  path('add_business/', views.addBusiness, name='add_business'),
  path('get_businesses/', views.getBusinesses, name='get_businesses'),
  path('get_business/<str:business_id>', views.getBusiness, name='get_business'),
  path('add_post/', views.addPost, name='add_post'),
  path('get_posts/', views.getPosts, name='get_posts'),
  path('get_post/<str:post_id>', views.getPost, name='get_post'),
  path('search/', views.search, name='search'),
  path('delete_neighborhood/<str:pk>', views.deleteNeighborhood, name='delete_neighborhood'),
  path('delete_post/<str:pk>', views.deletePost, name='delete_post'),
  path('add_neighborhood/', views.addNeighborhood, name='add_neighborhood'),

]