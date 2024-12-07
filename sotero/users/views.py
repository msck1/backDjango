from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuarios
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    senha = request.data.get('senha')

    try:
        usuario = Usuarios.objects.get(email=email)
        if usuario.senha == senha:
            return Response({'message': 'Login successful', 'user_id': usuario.id})
        else:
            return Response({'error': 'Invalid password'}, status=401)
    except Usuarios.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

@api_view(['POST'])
def logout_user(request):
    return Response({'message': 'Logout successful'})
