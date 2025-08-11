from rest_framework import serializers
from . models import *

class RegisterationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=128,
        write_only=True,
        style={"input_type":"password"})
    
    class Meta:
        model=User
        fields=["username","password"]

    def create(self, validated_data):
        password=validated_data.pop("password")
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user 

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        style={"input_type": "password"}
    )