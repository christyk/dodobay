from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.abstract.serializers import AbstractSerializer
from api.listing.models import Listing, Offer, Comment
from api.user.models import User
from api.user.serializers import UserSafeSerializer
from api.item.models import Item
from api.item.serializers import ItemSerializer

class ListingSerializer(AbstractSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    item = serializers.SlugRelatedField(queryset=Item.objects.all(), slug_field='unique_entry_id')
    watched = serializers.SerializerMethodField()
    watch_count = serializers.SerializerMethodField()

    def validate_user(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a listing for another user.")
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = User.objects.get_object_by_public_id(rep['user'])
        item = Item.objects.get(pk=rep['item'])
        rep['user'] = UserSafeSerializer(user).data
        rep['item'] = ItemSerializer(item).data
        return rep
        
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True

        instance = super().update(instance, validated_data)

        return instance
    
    def get_watched(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_watched(instance)
    
    def get_watch_count(self, instance):
        return instance.watched_by.count()
    
    class Meta:
        model = Listing
        fields = ['id', 'user', 'item', 'ask_bells', 'ask_tickets', 'ask_wishlist', 'watched', 'watch_count', 'status', 'edited', 'created', 'updated']
        read_only_fields = ['edited']


class OfferSerializer(AbstractSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    listing = serializers.SlugRelatedField(queryset=Listing.objects.all(), slug_field='public_id')

    def validate_user(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't make an offer for another user.")
        listing = Listing.objects.get_object_by_public_id(self._kwargs['data']['listing'])
        if listing.user == value:
            raise ValidationError("You can't place offer on your own listing.")
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = User.objects.get_object_by_public_id(rep['user'])
        rep['user'] = UserSafeSerializer(user).data
        return rep
    
    def validate_listing(self, value):
        if self.instance:
            return self.instance.listing
        return value
        
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True

        instance = super().update(instance, validated_data)

        return instance
    
    class Meta:
        model = Offer
        fields = ['id', 'user', 'listing', 'offer_bells', 'offer_tickets', 'offer_wishlist', 'status', 'edited', 'created', 'updated']
        read_only_fields = ['edited']


class CommentSerializer(AbstractSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    listing = serializers.SlugRelatedField(queryset=Listing.objects.all(), slug_field='public_id')

    def validate_user(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a comment for another user.")
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = User.objects.get_object_by_public_id(rep['user'])
        rep['user'] = UserSafeSerializer(user).data
        return rep
    
    def validate_listing(self, value):
        if self.instance:
            return self.instance.listing
        return value
        
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True

        instance = super().update(instance, validated_data)

        return instance
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'listing', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']