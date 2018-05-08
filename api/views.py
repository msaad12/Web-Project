from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, LoginSerializer, SignupSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserLoginAPIView(APIView):

    permission_classes = (AllowAny,)
    response_serializer = UserSerializer
    http_method_names = ['post', ]
    user = None

    def post(self, request, **kwargs):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user = authenticate(**serializer.data)

                if user is not None:
                        user_token, created = Token.objects.get_or_create(user=user)
                        return Response({'user': self.response_serializer(user).data, 'token': user_token.key},
                                        status=status.HTTP_200_OK)
                return Response({'success': False, 'error': "user is not authenticated"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error': ex.__str__(), 'success': False})


class UserSignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny, )
    response_serializer = UserSerializer
    http_method_names = ['post', ]
    model = User

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            key = self.after_create(serializer)
            return Response({'user': self.response_serializer(serializer.instance).data, 'token': key, 'success': True})
        except Exception as ex:
            return Response({'error': ex.__str__(), 'success': False})

    def after_create(self, serializer):

        try:
            if serializer.instance:
                user = serializer.instance
                user.set_password(serializer.validated_data.get('password'))
                user.is_active = True
                user.save()
                user_token, created = Token.objects.get_or_create(user=serializer.instance)
                return user_token.key
        except Exception as ex:
            raise Exception(ex.__str__())
#https://knowledge.geotrust.com/support/knowledge-base/index?page=content&id=SO27347&pmv=print&actp=PRINT&viewlocale=en_US