from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS: #GET
            return True
        
        if request.user and request.user.is_authenticated: #POST PUT, PATCH, DELETE

            if view.basename in ["listing", "listing-comment", "listing-offer"]:
                return True

            if view.basename in ["item"]:
                if request.method in ["POST"]:
                    if view.action in ["wish", "remove_wish"]:
                        return True
                        
            if view.basename in ["user"]:
                if request.method in ["PATCH"]:
                    return request._user.public_id.hex == view.kwargs['pk'] or request.user.is_superuser
        
        return False  

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS: #GET
            return True
        
        if request.user and request.user.is_authenticated: #POST, PUT, PATCH, DELETE

            if view.action in ["wish", "remove_wish", "watch", "remove_watch", "accept", "reject", "fulfill", "cancel"]:
                return request.user.is_authenticated
            if view.basename in ["listing", "listing-comment", "listing-offer"]:
                return request.user == obj.user or (request.user.is_superuser and request.method in ["DELETE"])

            if view.basename in ["user"]:
                if request.method in ["PATCH"]:
                    return request.user.id == obj.id or request.user.is_superuser

        return False