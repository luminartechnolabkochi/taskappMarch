

from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Task


class UserSerializer(serializers.ModelSerializer):

    password1=serializers.CharField(write_only=True)

    password2=serializers.CharField(write_only=True)

    password=serializers.CharField(read_only=True)


    class Meta:

        model=User

        fields=["username","email","password1","password2","password"]

    def validate(self, data):
        if data.get("password1") != data.get("password2"):

            raise serializers.ValidationError("password mismatch")
        return data

    def create(self, validated_data):

        password1=validated_data.pop("password1")
        password2=validated_data.pop("password2")

        return User.objects.create_user(**validated_data,password=password1)
    


class TaskSerializer(serializers.ModelSerializer):


    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=["id","owner","created_date"]