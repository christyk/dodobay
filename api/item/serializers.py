from rest_framework import serializers
from api.listing.models import Listing
from .models import Category, Item, \
    Accessory, Achievement, Artwork, Bag, Bottom, CeilingDecor, ClothingOther, \
    Construction, DressUp, Fencing, Fish, Floor, Fossil, Gyroid, Headwear, Houseware, \
    Insect, InteriorStructure, MessageCard, Miscellaneous, Music, Other, ParadisePlanning, \
    Photo, Poster, Reaction, Recipe, Rug, SeasonEvent, SeaCreature, Shoes, Socks, \
    SpecialNpc, ToolGood, Top, Umbrella, Villager, Wallpaper, WallMounted

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name', 'tradable']

class ItemSerializer(serializers.ModelSerializer):
    wished = serializers.SerializerMethodField()
    wish_count = serializers.SerializerMethodField()
    listing_count = serializers.SerializerMethodField()

    def get_wished(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_wished(instance)
    
    def get_wish_count(self, instance):
        return instance.wished_by.count()
    
    def get_listing_count(self, instance):
        return Listing.objects.filter(item=instance).count()
    
    class Meta:
        model = Item
        fields = ['unique_entry_id', 'name', 'image', 'category', 'variation', 'color_1', 'color_2', \
                  'source', 'season_event', 'buy', 'sell', 'wished', 'wish_count', 'listing_count']

class AccessoryDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Accessory
        fields = '__all__'

class AchievementDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Achievement
        fields = '__all__'

class ArtworkDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artwork
        fields = '__all__'

class BagDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bag
        fields = '__all__'

class BottomDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bottom
        fields = '__all__'

class CeilingDecorDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CeilingDecor
        fields = '__all__'

class ClothingOtherDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClothingOther
        fields = '__all__'

class ConstructionDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Construction
        fields = '__all__'

class DressUpDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DressUp
        fields = '__all__'

class FencingDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fencing
        fields = '__all__'

class FishDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fish
        fields = '__all__'

class FloorDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Floor
        fields = '__all__'

class FossilDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fossil
        fields = '__all__'

class GyroidDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gyroid

class HeadwearDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Headwear
        fields = '__all__'

class HousewareDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Houseware
        fields = '__all__'

class InsectDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Insect
        fields = '__all__'

class InteriorStructureDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InteriorStructure
        fields = '__all__'

class MessageCardDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MessageCard
        fields = '__all__'

class MiscellaneousDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Miscellaneous
        fields = '__all__'

class MusicDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = '__all__'

class OtherDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Other
        fields = '__all__'

class ParadisePlanningDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParadisePlanning
        fields = '__all__'

class PhotoDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = '__all__'

class PosterDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Poster
        fields = '__all__'

class ReactionDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reaction
        fields = '__all__'

class RecipeDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = '__all__'

class RugDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rug
        fields = '__all__'

class SeasonEventDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SeasonEvent
        fields = '__all__'

class SeaCreatureDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SeaCreature
        fields = '__all__'

class ShoesDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shoes
        fields = '__all__'

class SocksDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Socks
        fields = '__all__'

class SpecialNpcDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpecialNpc
        fields = '__all__'

class ToolGoodDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToolGood
        fields = '__all__'

class TopDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Top
        fields = '__all__'

class UmbrellaDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Umbrella
        fields = '__all__'

class VillagerDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Villager
        fields = '__all__'

class WallpaperDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wallpaper
        fields = '__all__'

class WallMountedDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WallMounted
        fields = '__all__'

