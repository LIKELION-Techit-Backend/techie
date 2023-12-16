
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Lecture,Course, Team
from rest_framework.views import APIView
from .serializers import MemberSerializer, TeamSerializer, LectureSerializer, CourseSerializer

class MemberAPI(APIView):
    def get(selft, request, id):
        try:
            member = Member.objects.get(id=id)
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        except:
            return Response({"message": "member not found"},status=status.HTTP_404_NOT_FOUND)       
        
    def put(self, request, id):
        try:
            query = Member.objects.get(id=id)
        except Member.DoesNotExist:
            return Response({'error' : {'message' : "member not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        member = MemberSerializer(query,data=request.data)
        if member.is_valid():
            member.save()
            return Response(member.data)
        return Response(member.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = Member.objects.get(id=id)
        result.delete()
        return Response(status=204)
    
class MemberListAPI(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        print(queryset)
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        member = MemberSerializer(data=request.data)
        
        if member.is_valid():
            if len(Member.objects.filter(email=request.data['email'])) == 0:
                member.save()
                return Response(member.data)
            else:
                return Response({"message": "email already exists"},status=status.HTTP_409_CONFLICT)        
        return Response(member.errors,status=status.HTTP_400_BAD_REQUEST)

class TeamListAPI(APIView):
    def get(self, request):
        queryset = Team.objects.all()
        print(queryset)
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)
    
class LectureListAPI(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)

class CourseAPI(APIView):
    def get(self, request, id):
        try:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except:
            return Response({"message": "course not found"},status=status.HTTP_404_NOT_FOUND)       
        
    def put(self, request, id):
        try:
            query = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({'error' : {'message' : "course not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        course = CourseSerializer(query,data=request.data)
        if course.is_valid():
            course.save()
            return Response(course.data)
        return Response(course.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        print(id)
        try:
            query = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({'error' : {'message' : "course not found!"}}, status = status.HTTP_404_NOT_FOUND)
        result = Course.objects.get(id=id)
        result.delete()
        return Response({'message': 'successfully deleted!'}, status=204)
    
        
    
class CourseListAPI(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        print(queryset)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        course = CourseSerializer(data=request.data)
        
        if course.is_valid():
            if len(Course.objects.filter(title=request.data['title'])) == 0:
                course.save()
                return Response(course.data)
            else:
                return Response({"message": "course already exists"},status=status.HTTP_409_CONFLICT)        
        return Response(course.errors,status=status.HTTP_400_BAD_REQUEST)

# 멋사 화이팅