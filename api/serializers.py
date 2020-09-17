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

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )

    class Meta:
        model = Item
        fields = ['image', 'name','detail']




class ItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'