from django.urls import path

from .views import signup, show_all, login, change_password, logout


urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('change_password/', change_password),
    path('users/', show_all),
]
