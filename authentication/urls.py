from django.urls import path
from authentication.views import login,register,create_cat_flutter,logout
app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('create-flutter/', create_cat_flutter, name='create_cat_flutter'),
    path('logout/', logout, name='logout'),
]