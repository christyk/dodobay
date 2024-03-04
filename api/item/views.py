from api.auth.permissions import UserPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from .models import Category, Item, \
    Accessory, Achievement, Artwork, Bag, Bottom, CeilingDecor, ClothingOther, \
    Construction, DressUp, Fencing, Fish, Floor, Fossil, Gyroid, Headwear, Houseware, \
    Insect, InteriorStructure, MessageCard, Miscellaneous, Music, Other, ParadisePlanning, \
    Photo, Poster, Reaction, Recipe, Rug, SeasonEvent, SeaCreature, Shoes, Socks, \
    SpecialNpc, ToolGood, Top, Umbrella, Villager, Wallpaper, WallMounted
from api.item.serializers import (
    CategorySerializer,
    ItemSerializer,
    AccessoryDetailSerializer, 
    AchievementDetailSerializer, 
    ArtworkDetailSerializer, 
    BagDetailSerializer, 
    BottomDetailSerializer, 
    CeilingDecorDetailSerializer, 
    ClothingOtherDetailSerializer, 
    ConstructionDetailSerializer, 
    DressUpDetailSerializer, 
    FencingDetailSerializer, 
    FishDetailSerializer, 
    FloorDetailSerializer, 
    FossilDetailSerializer, 
    GyroidDetailSerializer, 
    HeadwearDetailSerializer, 
    HousewareDetailSerializer, 
    InsectDetailSerializer, 
    InteriorStructureDetailSerializer, 
    MessageCardDetailSerializer, 
    MiscellaneousDetailSerializer, 
    MusicDetailSerializer, 
    OtherDetailSerializer, 
    ParadisePlanningDetailSerializer, 
    PhotoDetailSerializer, 
    PosterDetailSerializer, 
    ReactionDetailSerializer, 
    RecipeDetailSerializer, 
    RugDetailSerializer, 
    SeasonEventDetailSerializer, 
    SeaCreatureDetailSerializer, 
    ShoesDetailSerializer, 
    SocksDetailSerializer, 
    SpecialNpcDetailSerializer, 
    ToolGoodDetailSerializer, 
    TopDetailSerializer, 
    UmbrellaDetailSerializer, 
    VillagerDetailSerializer, 
    WallpaperDetailSerializer, 
    WallMountedDetailSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ('get')
    permission_classes = (UserPermission,)
    serializer_class = CategorySerializer
    

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    http_method_names = ('get', 'post')
    permission_classes = (UserPermission,)
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'color_1', 'color_2', 'source', 'season_event']
    search_fields = ['name', 'category__name', 'color_1', 'color_2', 'variation', 'source', 'season_event']
    ordering_fields = ['name']

    @action (methods=['POST'], detail=True)
    def wish(self, request, *args, **kwargs):
        item = self.get_object()
        user = self.request.user
        user.add_wish(item)
        serializer = self.serializer_class(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action (methods=['POST'], detail=True)
    def remove_wish(self, request, *args, **kwargs):
        item = self.get_object()
        user = self.request.user
        user.remove_wish(item)
        serializer = self.serializer_class(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemDetailViewSet(ModelViewSet):
    http_method_names = ('get')
    permission_classes = (UserPermission,)

    CLASS_CHOICES = {
        'Accessory' : Accessory, 
        'Achievement' : Achievement, 
        'Artwork' : Artwork, 
        'Bag' : Bag, 
        'Bottom' : Bottom, 
        'CeilingDecor' : CeilingDecor, 
        'ClothingOther' : ClothingOther, 
        'Construction' : Construction, 
        'DressUp' : DressUp, 
        'Fencing' : Fencing, 
        'Fish' : Fish, 
        'Floor' : Floor, 
        'Fossil' : Fossil, 
        'Gyroid' : Gyroid, 
        'Headwear' : Headwear, 
        'Houseware' : Houseware, 
        'Insect' : Insect, 
        'InteriorStructure' : InteriorStructure, 
        'MessageCard' : MessageCard, 
        'Miscellaneous' : Miscellaneous, 
        'Music' : Music, 
        'Other' : Other, 
        'ParadisePlanning' : ParadisePlanning, 
        'Photo' : Photo, 
        'Poster' : Poster, 
        'Reaction' : Reaction, 
        'Recipe' : Recipe, 
        'Rug' : Rug, 
        'SeasonEvent' : SeasonEvent, 
        'SeaCreature' : SeaCreature, 
        'Shoes' : Shoes, 
        'Socks' : Socks, 
        'SpecialNpc' : SpecialNpc, 
        'ToolGood' : ToolGood, 
        'Top' : Top, 
        'Umbrella' : Umbrella, 
        'Villager' : Villager, 
        'Wallpaper' : Wallpaper, 
        'WallMounted' : WallMounted,
    }
    
    SERIALIZER_CHOICES = {
        'Accessory' : AccessoryDetailSerializer, 
        'Achievement' : AchievementDetailSerializer, 
        'Artwork' : ArtworkDetailSerializer, 
        'Bag' : BagDetailSerializer, 
        'Bottom' : BottomDetailSerializer, 
        'CeilingDecor' : CeilingDecorDetailSerializer, 
        'ClothingOther' : ClothingOtherDetailSerializer, 
        'Construction' : ConstructionDetailSerializer, 
        'DressUp' : DressUpDetailSerializer, 
        'Fencing' : FencingDetailSerializer, 
        'Fish' : FishDetailSerializer, 
        'Floor' : FloorDetailSerializer, 
        'Fossil' : FossilDetailSerializer, 
        'Gyroid' : GyroidDetailSerializer, 
        'Headwear' : HeadwearDetailSerializer, 
        'Houseware' : HousewareDetailSerializer, 
        'Insect' : InsectDetailSerializer, 
        'InteriorStructure' : InteriorStructureDetailSerializer, 
        'MessageCard' : MessageCardDetailSerializer, 
        'Miscellaneous' : MiscellaneousDetailSerializer, 
        'Music' : MusicDetailSerializer, 
        'Other' : OtherDetailSerializer, 
        'ParadisePlanning' : ParadisePlanningDetailSerializer, 
        'Photo' : PhotoDetailSerializer, 
        'Poster' : PosterDetailSerializer, 
        'Reaction' : ReactionDetailSerializer, 
        'Recipe' : RecipeDetailSerializer, 
        'Rug' : RugDetailSerializer, 
        'SeasonEvent' : SeasonEventDetailSerializer, 
        'SeaCreature' : SeaCreatureDetailSerializer, 
        'Shoes' : ShoesDetailSerializer, 
        'Socks' : SocksDetailSerializer, 
        'SpecialNpc' : SpecialNpcDetailSerializer, 
        'ToolGood' : ToolGoodDetailSerializer, 
        'Top' : TopDetailSerializer, 
        'Umbrella' : UmbrellaDetailSerializer, 
        'Villager' : VillagerDetailSerializer, 
        'Wallpaper' : WallpaperDetailSerializer, 
        'WallMounted' : WallMountedDetailSerializer,
    }

    def get_queryset(self, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs.get('pk'))
        class_name = self.CLASS_CHOICES[item.category.class_name]
        return class_name.objects.all()
    
    def get_serializer_class(self, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs.get('pk'))
        return self.SERIALIZER_CHOICES[item.category.class_name]
