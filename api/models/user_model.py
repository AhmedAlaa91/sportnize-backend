# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
        null=True,
    )
    username = models.CharField(_("Username"), max_length=150, blank=True, unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True, null=True,)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True,)
    phone = models.CharField(max_length=255, blank=True, null=True,)
    timestamp = models.DateTimeField(auto_now_add=True)
    height = models.FloatField(_("Height"), blank=True, null=True,)
    weight = models.FloatField(_("Weight"), blank=True, null=True,)
    height_unit = models.CharField(_("Height Unit"), max_length=100, blank=True, null=True,)
    weight_unit = models.CharField(_("Weight Unit"), max_length=100, blank=True, null=True,)
    age = models.SmallIntegerField(_("Age"), blank=True, null=True,)
    school = models.CharField(_("School"), max_length=150, blank=True, null=True,)
    sport = models.CharField(_("Sport"), max_length=150, blank=True, null=True,)
    address = models.CharField(
        _("Address"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_admin = models.BooleanField(
        _("Admin"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as an Admin. ",
        ),
        null=True,
    )
    is_client = models.BooleanField(
        _("Client"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as a Client. ",
        ),
        null=True,
    )
    USER_TYPE_CHOICES = (
        (1, "Admin"),
        (2, "Client"),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES,
        null=True,
        verbose_name=_("User Type"),
        help_text=_(
            "User Role in A system ",
        ),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts.",
        ),
        null=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
        null=True,
    )
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return "{} <{}>".format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
