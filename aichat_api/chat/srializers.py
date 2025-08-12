from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class RegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        style={"input_type": "password"}
    )
    
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError({"error": "Username and password are required"})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid username or password"})

        if not check_password(password, user.password):
            raise serializers.ValidationError({"error": "Invalid username or password"})

        attrs['user'] = user
        return attrs
