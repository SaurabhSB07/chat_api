from rest_framework import serializers
from .models import User,Chat
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone


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
            'message': "Login Successfull",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class ChatSerializer(serializers.ModelSerializer):
    message = serializers.CharField(write_only=True)  
    response = serializers.CharField(read_only=True)  # read_only which server generates
    timestamp = serializers.DateTimeField(read_only=True)  # Automatically set when saving
    
    class Meta:
        model = Chat
        fields = ['message', 'response','timestamp']  

    def create(self, validated_data):
        user = self.context['request'].user
        if user.tokens < 100:
            raise serializers.ValidationError("Not enough tokens to send a message.")
        user.tokens -= 100
        user.save()
        
        ai_response = "This is a dummy AI response."

        #  Save chat history
        chat = Chat.objects.create(
            user=user,
            message=validated_data['message'],
            response=ai_response,
            timestamp=timezone.now(),
            
        )
  
        return chat  

class TokenBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'tokens']
        read_only_fields = ['username', 'tokens']