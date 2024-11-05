from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from authentication.api.serializers import RegisterSerializer, UserInfoWithToken

User = get_user_model()


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginUserView(TokenObtainPairView):
    serializer_class = UserInfoWithToken