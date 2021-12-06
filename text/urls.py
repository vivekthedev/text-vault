from django.urls import path
from .views import home, textview, update,delete,download,reset_pass,grant_access
app_name = 'text'

urlpatterns = [
    path('', home, name='home'),
    path('5ef94d85f05b2ed6d8f/', update, name='update'),
    path('194758952d55b72e14a/', delete, name='delete'),
    path('7a6d4be6bf8c918260c/', reset_pass, name='reset_pass'),
    path('c4e2ec3b5e82818b55f/', grant_access, name='grant_access'),
    path('9e8c85ec4ea02fd4394/', download, name='download'),
    path('<slug:slug>/', textview, name='textview'),
]
handler404 = "text.views.handle_404_view"