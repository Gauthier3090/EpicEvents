from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

MANAGEMENT = 'MANAGEMENT'
SALES = 'SALES'
SUPPORT = 'SUPPORT'


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, is_staff=False, is_admin=False, is_active=True):
        if phone is None:
            raise TypeError('Users must have a phone number.')

        user = self.model(phone=phone)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)

        return user


def create_staff_user(self, phone, password):
    """
    Creates and saves a staff user with the given email and password.
    """
    user = self.create_user(
        phone,
        password=password,
        is_staff=True
    )
    #    user.staff = True
    user.save(using=self._db)
    return user


def create_superuser(self, phone, password):
    """
    Creates and saves a superuser with the given email and password.
    """
    user = self.create_user(
        phone=phone,
        password=password,
        is_staff=True,
        is_admin=True
    )
    # user.staff = True
    # user.admin = True
    # user.active=True
    user.save(using=self._db)
    return user


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(
        choices=[
            (MANAGEMENT, MANAGEMENT),
            (SALES, SALES),
            (SUPPORT, SUPPORT)
        ],
        max_length=10,
        default=MANAGEMENT
    )
    email = models.EmailField(max_length=200, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'mobile', 'password', 'team']

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.team})"

    def save(self, *args, **kwargs):
        if self.team == MANAGEMENT:
            self.is_superuser = True
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        user = super(User, self)
        user.save()

        return user
