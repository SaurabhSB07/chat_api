from rest_framework import generics
from .models import User,Chat
from .serializers import RegisterSerializer, LoginSerializer,ChatSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            message = serializer.validated_data.get('message')
            # Dummy AI response
            response_text = "This is a dummy AI response."

            # to Save a chat history
            Chat.objects.create(user=user, message=message, response=response_text)

            return Response({"AI": response_text})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
