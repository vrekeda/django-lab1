from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/lab/tasks/', consumers.TasksConsumer.as_asgi()),
    re_path(r'ws/lab/(?P<language_id>\d+)/$', consumers.ChatConsumer.as_asgi())
]
