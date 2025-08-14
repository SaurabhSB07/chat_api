from .serializers import RegisterSerializer, LoginSerializer,ChatSerializer,TokenBalanceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny

# Register View
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successfull"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#chat view 
class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data, context={'request': request})
        user=request.user
        if serializer.is_valid():
            
            chat = serializer.save()
            return Response(
                {
                    "message": chat.message,
                    "response": chat.response,
                    "timestamp": chat.timestamp,
                    "remaining_tokens": user.tokens
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#token balance
class TokenBalanceApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = TokenBalanceSerializer(request.user)
        return Response(serializer.data)



        
