from api.user.models import User
from api.abstract.serializers import AbstractSerializer
from rest_framework import serializers
from django.conf import settings

class UserSerializer(AbstractSerializer):
    listings_count = serializers.SerializerMethodField()

    def get_listings_count(self, instance):
        return instance.listing_set.all().count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("avatar")==None:
            representation["avatar"] = settings.DEFAULT_AVATAR_URL
            return representation
        if settings.DEBUG:  # debug enabled for dev
            request = self.context.get("request")
            representation["avatar"] = request.build_absolute_uri(
                representation["avatar"]
            )
        return representation
    
    class Meta:
        model = User
        fields = ['id', 'username', 'villager_name', 'email', 'island_name', 'hemisphere', 'friend_code', 'avatar', 'wishlist', 'watchlist', 'listings_count', 'is_active', 'is_staff', 'is_superuser', 'created', 'updated']
        read_only_field = ['is_active']

class UserSafeSerializer(UserSerializer):
    class Meta:
        model = User
        fields=['id', 'username', 'villager_name', 'island_name', 'hemisphere', 'friend_code', 'avatar', 'wishlist', 'listings_count']
        read_only_field = ['is_active']