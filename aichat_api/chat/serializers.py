from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

from rest_framework import serializers
from django.utils import timezone
from .models import Chat
from django.contrib.auth import get_user_model

User = get_user_model()  # Ensures compatibility if we ever switch to a custom user model

class ChatSerializer(serializers.ModelSerializer):
    # We only take `message` from the user input, everything else is auto-generated
    message = serializers.CharField(write_only=True)  # write_only → client sends it, we don’t send it back raw

    # Fields we return to the client
    response = serializers.CharField(read_only=True)  # read_only → server generates it
    timestamp = serializers.DateTimeField(read_only=True)  # Automatically set when saving

    class Meta:
        model = Chat
        fields = ['message', 'response', 'timestamp']  # Minimal API — clean & focused

    def create(self, validated_data):
        """
        Handles:
        - Token deduction
        - AI response generation (dummy)
        - Saving chat history
        """
        user = self.context['request'].user
        if user.tokens < 100:
            raise serializers.ValidationError("Not enough tokens to send a message.")
        user.tokens -= 100
        user.save()

        #  Generate dummy AI response (replace with real AI integration later)
        ai_response = "This is a dummy AI response."

        #  Save chat history
        chat = Chat.objects.create(
            user=user,
            message=validated_data['message'],
            response=ai_response,
            timestamp=timezone.now()
        )
        return chat  
