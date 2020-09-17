from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from items.models import Item, FavoriteItem
from .serializers import RegisterSerializer,ItemListSerializer,ItemDetailsSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

from rest_framework.permissions import AllowAny

# Create your views here.

class Register(CreateAPIView):
	serializer_class = RegisterSerializer


class ItemList(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter,OrderingFilter,]
	search_fields = ['name']
	permission_classes = [AllowAny]

class ItemDetail(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
