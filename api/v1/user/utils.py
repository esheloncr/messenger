from django.http import Http404


def is_authenticated(func):
    """
    Wrap views function and verify that user is authenticated.
    """
    def wrapper(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise Http404
        return func(self, request, *args, **kwargs)
    return wrapper
