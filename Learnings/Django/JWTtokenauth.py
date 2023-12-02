# Authentication --> CAn bbe done using oauth or jwt
# !JSON Web Token Authentication -- JWT
# !Simple JWT

# pip install djangorestframework-simplejwt
# Configure in settings.py in default Authenication classes for globally execution
# in urls.py  , --> from jwt views import Tokenobtaonpairviews, and , tokenrefreshview can also verify

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]

# JWT default settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME':timedelta(days=1),
}