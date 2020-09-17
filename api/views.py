from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from items.models import Item, FavoriteItem
from .serializers import RegisterSerializer

# Create your views here.

class Register(CreateAPIView):
	serializer_class = RegisterSerializer
