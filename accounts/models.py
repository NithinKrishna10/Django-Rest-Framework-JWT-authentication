from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

# Create your models here.

class UserAccountManager(BaseUserManager):

    def create_user(self,full_name, email, password=None):

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            full_name = full_name,
            email=email,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,full_name, email, password=None):

        user = self.create_user( 
                full_name= full_name,
                email = email,
                password=password,
              
            )
        user.is_admin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    image=models.ImageField(upload_to='images',default='images\Vladimir_Putin_17-11-2021_(cropped).jpg')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin