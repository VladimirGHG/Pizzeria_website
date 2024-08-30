from django.urls import path

from .views import register, login_user, logout_user, ProfileView, ProfileListView, UpdateProfileView, DeleteUserView

app_name = "users"
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login_user"),
    path("log-out/", logout_user, name="log_out_user"),
    path("profiles/list", ProfileListView.as_view(), name="profile-list"),
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("profile/update/<int:id>", UpdateProfileView.as_view(), name="update_profile"),
    path("profile/delete/<int:id>", DeleteUserView.as_view(), name="delete_profile"),
]
