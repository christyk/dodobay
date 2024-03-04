from rest_framework import routers
from rest_framework_nested import routers

from api.user.views import UserViewSet
from api.auth.views import RegisterViewSet, LoginViewSet, RefreshViewSet, LogoutViewSet
from api.item.views import CategoryViewSet, ItemViewSet, ItemDetailViewSet
from api.listing.views import ListingViewSet, OfferViewSet,CommentViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'user', UserViewSet, basename='user')

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'auth/logout', LogoutViewSet, basename='auth-logout')

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'item', ItemViewSet, basename='item')
router.register(r'item-detail', ItemDetailViewSet, basename='item-detail')

router.register(r'listing', ListingViewSet, basename='listing')

listing_router = routers.NestedDefaultRouter(router, r'listing', lookup='listing')
listing_router.register(r'comment', CommentViewSet, basename='listing-comment')
listing_router.register(r'offer', OfferViewSet, basename='listing-offer')

user_router = routers.NestedDefaultRouter(router, r'user', lookup='user')
user_router.register(r'listing', ListingViewSet, basename='user-listing')
user_router.register(r'comment', CommentViewSet, basename='user-comment')
user_router.register(r'offer', OfferViewSet, basename='user-offer')

urlpatterns = [
    *router.urls,
    *listing_router.urls,
    *user_router.urls,
]