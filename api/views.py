
from django.shortcuts import render
from rest_framework.response import Response
from .models import Member,Lecture,Course
from rest_framework.views import APIView
from .serializers import MemberSerializer,LectureSerializer,CourseSerializer

class MemberListAPI(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        print(queryset)
        print("ASDASWDASDASD")
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)
    
class LectureListAPI(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)

class CourseListAPI(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        print(queryset)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
