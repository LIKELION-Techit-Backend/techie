#product/serializers.py
from rest_framework import serializers
from .models import Member,Lecture,Course

class MemberSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Member
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Lecture
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Course
        fields = '__all__' 
