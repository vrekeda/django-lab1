from django.urls import path
from lab1_app import views
from lab1_app.models import ConnectedUsers

urlpatterns = [
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:language_id>/', views.room, name='language_id'),
]


ConnectedUsers.objects.all().delete()
