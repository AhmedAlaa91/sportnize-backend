# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from api.models import User


class AddUserForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "age",
            "weight",
            "height",
            "weight_unit",
            "height_unit",
            "school",
            "sport",
            "is_client",
            "is_superuser",
            "is_active",
            "is_staff",
            "user_type",
            "is_admin",
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "is_admin",
            "is_client",
            "is_superuser",
            "is_active",
            "is_staff",
            "user_type",
            "weight_unit",
            "height_unit",
            "age",
            "weight",
            "height",
            "school",
            "sport",
        )

    def clean_password(self):
        # Password can't be changed in the admin
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "timestamp",
        "age",
        "weight",
        "height",
        "weight_unit",
        "height_unit",
        "school",
        "sport",
        "is_client",
        "is_admin",
    )
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": ("first_name", "last_name", "phone", "address"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_client",
                    "user_type",
                    "is_staff",
                    "age",
                    "weight",
                    "height",
                    "school",
                    "sport",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "user_type",
                    "phone",
                    "address",
                    "is_active",
                    "is_admin",
                    "is_client",
                    "age",
                    "weight",
                    "height",
                    "school",
                    "sport",
                    "weight_unit",
                    "height_unit",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email", "first_name", "last_name")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
