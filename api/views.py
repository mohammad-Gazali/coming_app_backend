from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.serializers import UserSerilizer



@api_view(["GET"])
def home(request: HttpRequest) -> Response:
    return Response({"message": "This is coming management api"})


@api_view(["GET"])
def masters(request: HttpRequest) -> Response:

    normal_users = User.objects.filter()

    data = UserSerilizer(normal_users, many=True).data

    return Response(data)



# ======================== JWT views =========================
# here we customize jwt payload, so we add the username to it.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer