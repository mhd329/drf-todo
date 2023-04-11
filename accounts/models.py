from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        error_messages={"unique": "이미 가입된 이메일입니다."},
    )
    is_superuser = models.BooleanField(default=False)
    joined_at = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()

    class Meta:
        db_table = "User"
