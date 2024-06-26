# -*- coding: utf-8 -*-
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        token["last_name"] = user.last_name
        token["age"] = user.age
        token["height"] = user.height
        token["weight"] = user.weight
        token["height_unit"] = user.height_unit
        token["weight_unit"] = user.weight_unit
        token["sport"] = user.sport
        token["school"] = user.school
        token["is_client"] = user.is_client
        # ...
        return token
