from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import Http404
from api.abstract.models import AbstractModel, AbstractManager

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.public_id, filename)

class UserManager(BaseUserManager, AbstractManager):
    def get_object_by_public_id(self, public_id):
        # Manually handle exceptions instead of get_object_or_404
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError, ValidationError):
            raise Http404
        
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email')
        if password is None:
            raise TypeError('Users must have a password')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        if username is None:
            raise TypeError('Superusers must have a username')
        if email is None:
            raise TypeError('Superusers must have an email')
        if password is None:
            raise TypeError('Superusers must have a password')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)

    villager_name = models.CharField(max_length=255, null=True)
    island_name = models.CharField(max_length=255, null=True, unique=True)
    hemisphere = models.CharField(max_length=1, choices=[('N', 'Northern'), ('S', 'Southern')], default='N')
    friend_code = models.CharField(max_length=14, null=True, unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    wishlist = models.ManyToManyField('api_item.Item', related_name='wished_by', blank=True)
    watchlist= models.ManyToManyField('api_listing.Listing', related_name='watched_by', blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def add_wish(self, item):
        return self.wishlist.add(item)
    
    def remove_wish(self, item):
        return self.wishlist.remove(item)
    
    def has_wished(self, item):
        return self.wishlist.contains(item)

    
    def add_watch(self, listing):
        return self.watchlist.add(listing)
    
    def remove_watch(self, listing):
        return self.watchlist.remove(listing)
    
    def has_watched(self, listing):
        return self.watchlist.contains(listing)


    def __str__(self):
        return f"{self.email}"