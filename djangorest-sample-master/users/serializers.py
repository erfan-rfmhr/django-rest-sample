from rest_framework import serializers
from users.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'phone', 'password')
        read_only_fields = ['is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

    def create(self, validated_data):

        return User.objects.create_user(phone=validated_data['phone'], password=validated_data['password'],
                                        name=validated_data['name'])

