from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
   
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=100,null=True)
    mother_name = models.CharField(max_length=100,null=True)
    address1 = models.CharField(max_length=100,null=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,default="demo.jpg")

    def __str__(self):
        return str(self.user.email)
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        ''' 
            existing all user  
        '''
        # for user in User.objects.all():
        #     Profile.objects.get_or_create(user=user)
    instance.profile.save()