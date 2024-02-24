from django.urls import path
from . import views #ここで先ほど作ったviews.pyを入れる

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:id>/delete', views.delete, name='delete')
]