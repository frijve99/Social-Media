from django.db import models
from ast import Pass
# from django.db import models
from django.contrib.auth import get_user_model
from numpy import blackman
from traitlets import default
import datetime
from django.utils import timezone


# Create your models here.

User = get_user_model()

GENDER_CHOICES=(
        ('Male','Male'),
        ('Female','Female')
    )

class Profile(models.Model):
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30,default='user')
    email = models.EmailField(max_length=100,blank=True)
    auth_token = models.CharField(max_length=100,blank=True )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    # password = models.CharField(max_length=100)
    id_user = models.IntegerField()
    firstname = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True)
    phonenumber = models.CharField(max_length=20,blank=True)
    country = models.CharField(max_length=20,blank=True)
    dob = models.DateField(default=timezone.now) 
    forget_pass_token = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True,default='Hey its me')
    profileimg = models.ImageField(upload_to = 'profile_images',default='profilepic.jpg')
    location = models.CharField(max_length=100,blank=True)
    

    def __str__(self) :
        return self.user.username

    def get_age(self):
        age = datetime.date.today()-self.dob
        return int((age).days/365.25)

