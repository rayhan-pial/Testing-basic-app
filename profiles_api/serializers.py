from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializing a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs= {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password',
                }
            }
        }

        def create(self, validated_data):
            """Create & return a new user"""
            user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password']
            )

            return user


class ProfilefeedSerializer(serializers.ModelSerializer):
    """serializers profile feed """

    class Meta:
        model = models.profileFeed
        fields = ['id', 'user_profile', 'status_text', 'created_on']
        extra_kwargs = {
            'user_profile' : {'read_only': True}
        }
