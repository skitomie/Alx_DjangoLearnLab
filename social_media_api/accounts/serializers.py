from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define serializer fields, including CharField for username and email
    serializers.CharField()
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create a new user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )

        # Create a token for the newly registered user
        Token.objects.create(user=user)

        return user
