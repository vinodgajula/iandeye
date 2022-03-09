from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="home"),
    path("create", create, name="create"),
    path("go-to-home", homePageView, name="homePage"),
    path("signup-board", signUpDashBoard, name="signup-board"),
    path("admin-signup-board", adminSignUpDashBoard, name="admin-signup-board"),
    path("login-board", loginDashBoard, name="login-board"),
    path("admin-login-board", adminLoginDashBoard, name="admin-login-board"),
    path("insert-user", insertUser, name="insert-user"),
    path("select-user", selectUser, name="select-user"),
    path("view-users", viewUsers, name="view-users"),

]