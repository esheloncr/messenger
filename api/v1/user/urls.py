from django.urls import path

from .views import UserDetailView, UserListView, UserCreateView, UserAuthenticateView


urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("login/", UserAuthenticateView.as_view(), name="login_user")
]
