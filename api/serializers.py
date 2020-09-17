from rest_framework import serializers
from rest_framework.reverse import reverse_lazy
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name','detail', 'added_by', 'favourited']

    def get_favourited(self, obj):
        hearts = FavoriteItem.objects.filter(item=obj)
        return hearts.count()

class FavoriteItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= FavoriteItem
        fields = ['user']



class ItemDetailsSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name','description' ,'added_by', 'favourited_by'] 

    def get_favourited_by(self, obj):
        item_obj = FavoriteItem.objects.filter(item=obj)
        #users = FavoriteItem.objects.filter(item=item_obj)
        users = FavoriteItemSerializer(item_obj, many = True).data
        return users
        
        


