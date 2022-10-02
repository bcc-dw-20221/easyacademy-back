from enum import unique
from pyexpat import model
from .models import Student, Teacher
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.utils import timezone

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["url", "username", "first_name", "last_name"]
        
class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "password"},
    )

    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}, "username" : {"read_only": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        validated_data["username"] = validated_data["first_name"]+str(timezone.now().year)
        return super(CreateUserSerializer, self).create(validated_data)


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
    user = CreateUserSerializer(required=True)

    class Meta:
        model = Student
        fields = [
            "url",
            "registration",
            "user",
            "foto_perfil",
        ]
        extra_kwargs = {"registration": {"read_only": True}}

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of perfil
        :return: returns a successfully created perfil record
        """
        user_data = validated_data.pop("user")
        user = CreateUserSerializer.create(
            CreateUserSerializer(), validated_data=user_data
        )
        if user.pk:
            student, created = Student.objects.update_or_create(
                user=user,
                foto_perfil=validated_data.pop("foto_perfil"),
                #ano-cod-id-user
                registration=str(timezone.now().year)+'11'+str(user.pk),
            )
            if created:
                return student
        else:
            user.delete()
        return Response({"message": "Não pude criar um novo perfil."}, status=406)
    

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    
    user = CreateUserSerializer(required=True)
    
    class Meta:
        model = Teacher
        fields = [
            "url",
            "user",
            "foto_perfil",
        ]

    def create(self, validated_data):
        user_data = validated_data["user"]
        user = CreateUserSerializer.create(
            CreateUserSerializer(), validated_data=user_data 
        )
        if user.pk:
            teacher, created, = Teacher.objects.update_or_create(
                user=user,
                foto_perfil=validated_data.pop("foto_perfil")
            )
            if created:
                return teacher
        else:
            user.delete()
        return Response({"message": "Não pude criar um novo usuário"}, status=406)

