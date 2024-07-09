from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone


# TODO и настроить так чтоб в будущем можно было регистрироваться с помощью либо эмейла, либо номера телефона
class CustomUserManager(BaseUserManager):
    # TODO username=None (generate username)
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Пользователь должен иметь логин!")

        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):  # email
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    from utils.utils import generate_random_username
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        default=generate_random_username,
        validators=[ASCIIUsernameValidator(), MinLengthValidator(5)],
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        swappable = "AUTH_USER_MODEL"


class UserEmail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emails")
    email = models.EmailField()
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField("Создание", auto_now_add=True)
    updated_at = models.DateTimeField("Обновление", auto_now=True)


class UserPhoneNumber(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="phone_numbers")
    phone_number = models.CharField(max_length=25)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField("Создание", auto_now_add=True)
    updated_at = models.DateTimeField("Обновление", auto_now=True)
