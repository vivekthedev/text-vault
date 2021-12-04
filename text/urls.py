from django.urls import path
from .views import home, textview, update,delete,download,reset_pass,grant_access
app_name = 'text'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', textview, name='textview'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
    path('reset_pass/', reset_pass, name='reset_pass'),
    path('grant_access/', grant_access, name='grant_access'),
    path('download/', download, name='download'),
]