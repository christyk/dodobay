from django.core.cache import cache
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from api.auth.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from api.abstract.views import AbstractViewSet
from api.listing.serializers import ListingSerializer, OfferSerializer, CommentSerializer
from api.listing.models import Listing, Offer, Comment
from api.user.models import User

###########################
##   Listing View Set    ##
###########################

class ListingViewSet(AbstractViewSet):
    permission_classes = (UserPermission,)
    http_method_names = ('get', 'post', 'patch', 'delete')
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user__public_id', 'item__unique_entry_id']
    search_fields = ['user__public_id', 'item__unique_entry_id']
    ordering_fields = ['-created']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.basename in ["listing"]:
            return Listing.objects.all()
        if self.basename in ["user-listing"]:
            user = User.objects.get_object_by_public_id(self.kwargs['user_pk'])
            return Listing.objects.filter(user__pk=user.pk)

    def get_object(self):
        obj = Listing.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        listing_objects = cache.get("listing_objects")
        if listing_objects is None:
            listing_objects = self.filter_queryset(self.get_queryset())
            cache.set("listing_objects", listing_objects)

        page = self.paginate_queryset(listing_objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(listing_objects, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user']=request.user.public_id.hex
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action (methods=['POST'], detail=True)
    def watch(self, request, *args, **kwargs):
        listing = self.get_object()
        user = self.request.user
        user.add_watch(listing)
        serializer = self.serializer_class(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action (methods=['POST'], detail=True)
    def remove_watch(self, request, *args, **kwargs):
        listing = self.get_object()
        user = self.request.user
        user.remove_watch(listing)
        serializer = self.serializer_class(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action (methods=['POST'], detail=True)
    def fulfill(self, request, *args, **kwargs):
        listing = self.get_object()
        if listing.user == request.user:
            if listing.status == 'F':
                return Response({"message": "Listing is already fulfilled"})
            if listing.status == 'C':
                return Response({"message": "Cannot fulfill a canceled listing"})
            listing.status = 'F'
            listing.save()
            serializer = self.serializer_class(listing)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Only the listing owner may fulfill a listing"})
    
    @action (methods=['POST'], detail=True)
    def cancel(self, request, *args, **kwargs):
        listing = self.get_object()
        if listing.user == request.user:
            if listing.status == 'F':
                return Response({"message": "Cannot cancel a fulfilled listing"})
            if listing.status == 'C':
                return Response({"message": "Listing is already canceled"})
            listing.status = 'C'
            listing.save()
            serializer = self.serializer_class(listing)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Only the listing owner may cancel a listing"})


#########################
##   Offer View Set    ##
#########################

class OfferViewSet(AbstractViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete')
    serializer_class = OfferSerializer
    permission_classes = (UserPermission, IsAuthenticated)

    def get_queryset(self):
        if self.basename in ["listing-offer"]:
            listing = Listing.objects.get_object_by_public_id(self.kwargs['listing_pk'])
            if listing.user == self.request.user or self.request.user.is_superuser:
                return Offer.objects.filter(listing__pk=listing.pk)
            return Offer.objects.filter(listing__pk=listing.pk, user__public_id=self.request.user.public_id)
        
        if self.basename in ["user-offer"]:
            user = User.objects.get_object_by_public_id(self.kwargs['user_pk'])
            if user.pk == self.request.user.pk or self.request.user.is_superuser:
                return Offer.objects.filter(user__pk=user.pk)
            return Offer.objects.none()
    
    def get_object(self):
        obj = Offer.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        if Offer.objects.filter(listing__public_id=self.kwargs['listing_pk'], status__in=['O', 'A', 'R']).count() > 1:
            return Response({"message": "You may only have 1 active offer per listing"})
        
        listing = Listing.objects.get_object_by_public_id(self.kwargs['listing_pk'])
        if 'offer_wishlist' in request.data:
            if request.data['offer_wishlist'] not in listing.user.wishlist.values_list('unique_entry_id', flat=True):
                return Response({"message": "Offered item not in listing user's wish list"})

        if listing.status in ['O']:
            data = request.data
            data['user']=request.user.public_id.hex
            data['listing']=self.kwargs['listing_pk']
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if listing.status == 'F':
            return Response({"message": "Cannot place offer on a fulfilled listing"})
        if listing.status == 'C':
            return Response({"message": "Cannot place offer on a canceled listing"})
        return Response ({"message": "Cannot place offer, listing status unknown"})
    
    @action (methods=['POST'], detail=True)
    def accept(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.listing.user == request.user:
            if offer.status in ['O', 'R']:
                offer.status = 'A'
                offer.save()
                serializer = self.serializer_class(offer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if offer.status == 'F':
                return Response({"message": "Cannot accept a fulfilled offer"})
            if offer.status == 'C':
                return Response({"message": "Cannot accept a canceled offer"})
            return Response ({"message": "Offer status unknown"})
        return Response({"message": "Only the listing owner may accept an offer"})
    
    @action (methods=['POST'], detail=True)
    def reject(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.listing.user == request.user:
            if offer.status in ['O', 'A']:
                offer.status = 'R'
                offer.save()
                serializer = self.serializer_class(offer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if offer.status == 'F':
                return Response({"message": "Cannot reject a fulfilled offer"})
            if offer.status == 'C':
                return Response({"message": "Cannot reject a canceled offer"})
            return Response ({"message": "Offer status unknown"})
        return Response({"message": "Only the listing owner may reject an offer"})
    
    @action (methods=['POST'], detail=True)
    def fulfill(self, request, *args, **kwargs):
        offer = self.get_object()
        if request.user in [offer.user, offer.listing.user]:
            if offer.status in ['A'] and offer.listing.status in ['O']:
                offer.status = 'F'
                offer.save()
                serializer = self.serializer_class(offer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if offer.status == 'R':
                return Response({"message": "Cannot fulfill a rejected offer"})
            if offer.status == 'F':
                return Response({"message": "Offer already fulfilled"})
            if offer.status == 'C':
                return Response({"message": "Cannot fulfill a canceled offer"})
            return Response ({"message": "Cannot fulfill offer, offer status unknown"})
        return Response({"message": "Only the listing or offer owner may fulfill an offer"})
    
    @action (methods=['POST'], detail=True)
    def cancel(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.user == request.user:
            if offer.status == 'F':
                return Response({"message": "Cannot cancel a fulfilled offer"})
            if offer.status == 'C':
                return Response({"message": "Offer already canceled"})
            offer.status = 'C'
            offer.save()
            serializer = self.serializer_class(offer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Only the offer owner may cancel an offer"})
    
###########################
##   Comment View Set    ##
###########################

class CommentViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'patch', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()
        
        if self.basename in ["listing-comment"]:
            listing_pk = self.kwargs['listing_pk']
            if listing_pk is None:
                return Http404
            return Comment.objects.filter(listing__public_id=listing_pk)
        
        if self.basename in ["user-comment"]:
            user = User.objects.get_object_by_public_id(self.kwargs['user_pk'])
            if user.pk == self.request.user.pk or self.request.user.is_superuser:
                objs= Comment.objects.filter(user__pk=user.pk)
                return objs
            return Comment.objects.none()
        
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data['user']=request.user.public_id.hex
        data['listing']=self.kwargs['listing_pk']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)