# -*- coding: utf-8 -*-

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from api.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "height",
            "weight",
            "age",
            "sport",
            "school",
            "height_unit",
            "weight_unit",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_client(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            height=validated_data["height"],
            weight=validated_data["weight"],
            age=validated_data["age"],
            sport=validated_data["sport"],
            school=validated_data["school"],
            height_unit=validated_data["height_unit"],
            weight_unit=validated_data["weight_unit"],
        )
        user.save()
        return user
