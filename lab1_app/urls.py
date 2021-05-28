from django.urls import path
from lab1_app import views
from lab1_app.models import ConnectedUsers

from .views import send_email_task, run_long_task, list_finished_tasks

urlpatterns = [
    path('run_task/send_email/', send_email_task),
    path('run_task/long_work/', run_long_task),
    path('list_finished_task/', list_finished_tasks),
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:language_id>/', views.room, name='language_id')
]


ConnectedUsers.objects.all().delete()
