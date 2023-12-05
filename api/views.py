from django.shortcuts import render
from rest_framework.response import Response
from .models import Member, Lecture
from rest_framework.views import APIView
from .serializers import MemberSerializer, LectureSerializer
class MemberListAPI(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        print(queryset)
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)
    
class LectureListAPI(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)