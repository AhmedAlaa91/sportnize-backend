# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name,
        last_name,
        phone,
        address,
        height,
        weight,
        age,
        school,
        username,
        height_unit,
        weight_unit,
        password=None,
        commit=True,
    ):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not first_name:
            raise ValueError(_("Users must have a first name"))
        if not last_name:
            raise ValueError(_("Users must have a last name"))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            height=height,
            age=age,
            weight=weight,
            school=school,
            username=username,
            height_unit=height_unit,
            weight_unit=weight_unit,
        )

        user.set_password(password)
        user.is_active = True
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        password,
        address,
        phone,
        height,
        weight,
        age,
        school,
        username,
        height_unit,
        weight_unit,
    ):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            height=height,
            age=age,
            weight=weight,
            school=school,
            username=username,
            height_unit=height_unit,
            weight_unit=weight_unit,
            commit=False,
        )
        user.is_admin = True
        user.user_type = 1
        user.save(using=self._db)
        return user

    def create_client(
        self,
        email,
        first_name,
        last_name,
        phone,
        address,
        password,
        height,
        weight,
        age,
        school,
        username,
        height_unit,
        weight_unit,
    ):
        """
        Creates and saves a Client USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            height=height,
            age=age,
            weight=weight,
            school=school,
            username=username,
            height_unit=height_unit,
            weight_unit=weight_unit,
            commit=False,
        )
        user.is_Client = True
        user.user_type = 2
        user.save(using=self._db)
        return user
