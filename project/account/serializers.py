from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer
from django.core import serializers as my_serializers
import json


def serialize_user(user):
    user_data = my_serializers.serialize('json', [user])
    user_json = json.loads(user_data)[0]['fields']
    return user_json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email']
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        # fields = ['id', 'user', 'name', 'email', 'data']
        fields = '__all__'

    # def create(self, validated_data):
    #     # Extract user data from the serializer
    #     user_data = validated_data.pop('user')

    #     # Create or update the associated User instance
    #     user_instance, created = User.objects.get_or_create(**user_data)

    #     # Create or update the Customer instance
    #     customer_instance, created = Customer.objects.update_or_create(
    #         user=user_instance,
    #         **validated_data
    #     )

    #     return customer_instance
