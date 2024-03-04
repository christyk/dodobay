from api.auth.permissions import UserPermission

from api.user.serializers import UserSerializer, UserSafeSerializer
from api.user.models import User
from api.abstract.views import AbstractViewSet

class UserViewSet(AbstractViewSet):
    http_method_names = ('get', 'patch')
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        if self.action in ['list'] or self.request.user.is_anonymous:
            return UserSafeSerializer
        if self.request._user.public_id.hex == self.kwargs['pk'] or self.request.user.is_superuser:
            return UserSerializer
        return UserSafeSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj