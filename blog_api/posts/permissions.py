from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #  Authenticated users can only see list view'''
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            #  SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True

        # Write permissions are only allowed to the author of a post
        #  We access the author field via obj.author and the current user with request.user.
        return obj.author == request.user
