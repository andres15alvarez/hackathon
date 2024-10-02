from django.urls import path

from user.views import UserListAPIView, UserDetailAPIView

app_name = "user"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("/me", UserDetailAPIView.as_view(), name="me"),
]
