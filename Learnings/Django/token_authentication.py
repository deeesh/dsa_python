# 
# todo Generate Token
# ? 1).using command python manage.py drf_create_token <username>
# this command will return API Token for the given user or Creates a Token if it does not exist
# ? 2). or by Exposing an API Endpoint
# ? 3). Using Signals

# INSTALLED-APPS = ['rest_framework.authtoken']

# How client can Ask/create token
# ? When using token authentication, you may want to provide a mechanism for clients to obtain
# ? a token given the username and password
# REST Framework provides a built in view to provide this behavior.
# To use it, add obtain_auth_token view to your URLconf

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('gettoken/', obtain_auth_token)
]

# Custom AUth token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
# !Using Signals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)