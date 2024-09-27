from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["last_login", "date_joined", "groups", "user_permissions"]
        extra_kwargs = {
            "password": {
                "read_only": True
            }
        }
