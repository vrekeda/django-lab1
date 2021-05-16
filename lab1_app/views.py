from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url


from .models import Language, Word, ConnectedUsers
from .serializers import LanguageSerializers, WordSerializer
from django.http import HttpResponse
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LanguageSerializers


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WordSerializer


def index(request):
    languages = [user for user in Language.objects.all()]
    return render(request, 'index.html', {
        'languages': languages
    })


def room(request, language_id):
    # Send article by id to user
    lang = Language.objects.get(id=language_id)
    languages_list = Language.objects.all()
    words = [word for word in Word.objects.filter(translate_from=language_id)]
    if lang:
        return render(request, 'room.html', {
            'language_id': language_id,
            'name': lang.name,
            'ukrainian_name': lang.ukrainian_name,
            'words': words,
            'languages_list': languages_list
        })
    else:
        return HttpResponse('Wrong language id')


def users_online(request):
    if request.user.is_authenticated:
        connected_users = [user for user in ConnectedUsers.objects.all()]
        return render(request, 'online.html', {
            'connected_users': connected_users
        })
