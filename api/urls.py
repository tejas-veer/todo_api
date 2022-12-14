from django.urls import path
from .views import *


urlpatterns = [
    path("tasks/", TaskList.as_view(), name="tasklist"),
    path("tasks/<str:pk>", TaskDetails.as_view(), name="task"),
    path("register/", UserRegister.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
]
