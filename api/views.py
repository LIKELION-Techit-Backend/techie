
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Lecture,Course, Team
from rest_framework.views import APIView
from .serializers import MemberSerializer, TeamSerializer, LectureSerializer, CourseSerializer

class MemberAPI(APIView):
    def get(self, request, id):
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
        
        member = MemberSerializer(query,data=request.data, partial=True)
        if member.is_valid():
            member.save()
            return Response(member.data)
        return Response(member.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Member.objects.get(id=id)
        except Member.DoesNotExist:
            return Response({'error' : {'message' : "member not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        result = Member.objects.get(id=id)
        result.delete()
        return Response({"message": "successfully deleted!"}, status=204)
    
class MemberListAPI(APIView):
    def get(self, request):
        queryset = Member.objects.all()
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
    
    
class TeamAPI(APIView):
    def get(self, request, id):
        try:
            team = Team.objects.get(id=id)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except:
            return Response({"message": "team not found"},status=status.HTTP_404_NOT_FOUND)       
        
    def put(self, request, id):
        try:
            query = Team.objects.get(id=id)
        except Team.DoesNotExist:
            return Response({'error' : {'message' : "team not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        team = TeamSerializer(query,data=request.data, partial=True)
        if team.is_valid():
            team.save()
            return Response(team.data)
        return Response(team.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Team.objects.get(id=id)
        except Team.DoesNotExist:
            return Response({'error' : {'message' : "team not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        result = Team.objects.get(id=id)
        result.delete()
        return Response({"message": "successfully deleted!"}, status=204)
class TeamListAPI(APIView):
    def get(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        team = TeamSerializer(data=request.data)
        if team.is_valid():
            try:
                Team.objects.get(team_name=request.data['team_name'])
                return Response({"message": "team already exists"},status=status.HTTP_409_CONFLICT)        
            except:
                team.save()
                return Response(team.data)
        return Response(team.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LectureListAPI(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        lecture = LectureSerializer(data=request.data)
        
        if lecture.is_valid():
            if len(Lecture.objects.filter(lecture_name=request.data['lecture_name'])) == 0:
                lecture.save()
                return Response(lecture.data)
            else:
                return Response({"message": "lecture id already exists"},status=status.HTTP_409_CONFLICT)        
        return Response(lecture.errors,status=status.HTTP_400_BAD_REQUEST)

    
class LectureAPI(APIView):
    def get(self, request, id):
        try:
            lecture = Lecture.objects.get(id=id)
            serializer = LectureSerializer(lecture)
            return Response(serializer.data)
        except:
            return Response({"message": "lecture not found"},status=status.HTTP_404_NOT_FOUND)       
        
    def put(self, request, id):
        try:
            query = Lecture.objects.get(id=id)
        except Lecture.DoesNotExist:
            return Response({'error' : {'message' : "lecture not found!"}}, status = status.HTTP_404_NOT_FOUND)
        
        lecture = LectureSerializer(query,data=request.data)
        if lecture.is_valid():
            lecture.save()
            return Response(lecture.data)
        return Response(lecture.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = Lecture.objects.get(id=id)
        result.delete()
        return Response({"message" : "successfully deleted"}, status=204)

class CourseListAPI(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        print(queryset)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
