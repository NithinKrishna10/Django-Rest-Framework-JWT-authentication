from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('full_name', 'email', 'password')




  def create(self, validated_data):
    user = User.objects.create_user(
      full_name=validated_data['full_name'],
      
      email=validated_data['email'],
      password=validated_data['password'],
    )

    return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'