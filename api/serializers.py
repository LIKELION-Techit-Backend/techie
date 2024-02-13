# product/serializers.py
from rest_framework import serializers
from .models import Member, Lecture, Course, Pending, Team, Taken


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taken
        fields = '__all__'


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    is_staff = serializers.BooleanField()
    team = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)


class PendingSerializer(serializers.Serializer):
    class Meta:
        model = Pending
        fields = '__all__'


class PendingQuerySerializer(serializers.Serializer):
    team_id = serializers.IntegerField()


class PendingResponseSerialzier(serializers.Serializer):
    member_id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    accept = serializers.BooleanField()


class SyncBodySerializer(serializers.Serializer):
    input = serializers.JSONField()
