from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone

import re

from django.contrib.auth import get_user_model

from EMPLOYEE.models import Department, Position, Employee

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), write_only=True)
    status = serializers.BooleanField(default=False, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'department', 'position', 'status',]


    def validate_password(self, value):
        if not re.search(r'[A-Z]', value):  
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[0-9]', value):  
            raise serializers.ValidationError("Password must contain at least one digit.")
        return value

    def create(self, validated_data):

        department = validated_data.pop('department')
        position = validated_data.pop('position')
        status = validated_data.pop('status')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )


        Employee.objects.create(
            user=user,
            name=user.first_name,
            surname=user.last_name,
            email=user.email,
            department=department,
            position=position,
            status=status
        )

        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

class UserInfoWithToken(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # Update the last_login field for the associated Employee
        try:
            employee = Employee.objects.get(user=self.user)
            employee.last_login = timezone.now()
            employee.save()
        except Employee.DoesNotExist:
            pass

        user_serializer = LoginSerializer(self.user)

        data.update(user_serializer.data)
        return data