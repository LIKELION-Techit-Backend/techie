import json
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Lecture, Course, Team, Taken, Pending
from rest_framework.views import APIView
from .serializers import LoginSerializer, MemberSerializer, TeamSerializer, LectureSerializer, CourseSerializer, TakenSerializer, CreateUserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


class MemberAPI(APIView):
    def get(self, request, id):
        try:
            member = Member.objects.get(id=id)
            team = TeamSerializer(member.team).data
            return Response({
                "id": member.id,
                "email": member.email,
                "first_name": member.first_name,
                "last_name": member.last_name,
                "team": team,
                "is_staff": member.is_staff
            }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "member not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            query = Member.objects.get(id=id)
        except Member.DoesNotExist:
            return Response({'error': {'message': "member not found!"}}, status=status.HTTP_404_NOT_FOUND)

        member = MemberSerializer(query, data=request.data, partial=True)
        if member.is_valid():
            member.save()
            return Response(member.data)
        return Response(member.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Member.objects.get(id=id)
        except Member.DoesNotExist:
            return Response({'error': {'message': "member not found!"}}, status=status.HTTP_404_NOT_FOUND)

        result = Member.objects.get(id=id)
        result.delete()
        return Response({"message": "successfully deleted!"}, status=204)


class MemberListAPI(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        return Response([{
            "id": member.id,
            "email": member.email,
            "first_name": member.first_name,
            "last_name": member.last_name,
            "team": TeamSerializer(member.team).data,
            "is_staff": member.is_staff
        } for member in queryset], status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CreateUserSerializer, responses={200: 'Success'})
    def post(self, request):
        data = request.data

        try:
            member = Member.objects.get(email=data['email'])
            return Response({"message": "email already exists"}, status=status.HTTP_409_CONFLICT)
        except Member.DoesNotExist:
            try:
                team = Team.objects.get(id=data['team'])
            except:
                return Response({"message": "team not found"}, status=status.HTTP_404_NOT_FOUND)
            if data['is_staff'] is True:
                member = Member.objects.create(
                    email=data['email'],
                    password=make_password(data['password']),
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    is_staff=True,
                    team=team
                )
                member.save()
            else:
                member = Member.objects.create(
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    is_staff=False
                )
                member.set_password(data['password'])
                member.save()
                Pending.objects.create(member=member, team=team)
            return Response({
                "id": member.id,
                "email": member.email,
                "first_name": member.first_name,
                "last_name": member.last_name,
                "team": team,
                "is_staff": member.is_staff
            }, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    @swagger_auto_schema(request_body=LoginSerializer, responses={200: 'Success'})
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']

        try:
            Member.objects.get(email=email)
        except Member.DoesNotExist:
            return Response({"message": "email doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        member = auth.authenticate(request, username=email, password=password)
        print(member)
        if member is not None:
            refresh = RefreshToken.for_user(member)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_data': {
                    "id": member.id,
                    "email": member.email,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "team": TeamSerializer(member.team).data,
                    "is_staff": member.is_staff
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)


class TeamAPI(APIView):
    def get(self, request, id):
        try:
            team = Team.objects.get(id=id)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except:
            return Response({"message": "team not found"}, status=status.HTTP_404_NOT_FOUND)


class TeamListAPI(APIView):
    def get(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)


class LectureListAPI(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        print("============================")
        lecture = LectureSerializer(data=request.data)

        if lecture.is_valid():
            if len(Lecture.objects.filter(lecture_name=request.data['lecture_name'])) == 0:
                lecture.save()
                return Response(lecture.data)
            else:
                return Response({"message": "lecture id already exists"}, status=status.HTTP_409_CONFLICT)
        return Response(lecture.errors, status=status.HTTP_400_BAD_REQUEST)


class LectureAPI(APIView):
    def get(self, request, id):
        try:
            lecture = Lecture.objects.get(id=id)
            serializer = LectureSerializer(lecture)
            return Response(serializer.data)
        except:
            return Response({"message": "lecture not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            query = Lecture.objects.get(id=id)
        except Lecture.DoesNotExist:
            return Response({'error': {'message': "lecture not found!"}}, status=status.HTTP_404_NOT_FOUND)

        lecture = LectureSerializer(query, data=request.data)
        if lecture.is_valid():
            lecture.save()
            return Response(lecture.data)
        return Response(lecture.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = Lecture.objects.get(id=id)
        result.delete()
        return Response({"message": "successfully deleted"}, status=204)


class CourseAPI(APIView):
    def get(self, request, id):
        try:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except:
            return Response({"message": "course not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            query = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({'error': {'message': "course not found!"}}, status=status.HTTP_404_NOT_FOUND)

        course = CourseSerializer(query, data=request.data)
        if course.is_valid():
            course.save()
            return Response(course.data)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({'error': {'message': "course not found!"}}, status=status.HTTP_404_NOT_FOUND)
        result = Course.objects.get(id=id)
        result.delete()
        return Response({'message': 'successfully deleted!'}, status=204)


class CourseListAPI(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        course = CourseSerializer(data=request.data)

        if course.is_valid():
            if len(Course.objects.filter(title=request.data['title'])) == 0:
                course.save()
                return Response(course.data)
            else:
                return Response({"message": "course already exists"}, status=status.HTTP_409_CONFLICT)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


class TakenAPI(APIView):
    def get(self, request, id):
        try:
            taken = Taken.objects.get(id=id)
            serializer = TakenSerializer(taken)
            return Response(serializer.data)
        except:
            return Response({"message": "taken course is not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            Taken.objects.get(id=id)
        except Taken.DoesNotExist:
            return Response({'error': {'message': "taken not found!"}}, status=status.HTTP_404_NOT_FOUND)

        result = Taken.objects.get(id=id)
        result.delete()
        return Response({"message": "successfully deleted!"}, status=status.HTTP_200_OK)


class TakenListAPI(APIView):
    def get(self, request):
        mid = request.GET.get('mid')
        if mid is not None:
            queryset = Taken.objects.filter(member=mid)
        else:
            queryset = Taken.objects.all()
        serializer = TakenSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        mid = request.data['mid']
        lid = request.data['lid']

        # check member
        try:
            member = Member.objects.get(id=mid)
        except Member.DoesNotExist:
            return Response({"message": "member does not exists"}, status=status.HTTP_404_NOT_FOUND)
        # check lecture
        try:
            lecture = Lecture.objects.get(id=lid)
        except Lecture.DoesNotExist:
            return Response({"message": "lecture does not exists"}, status=status.HTTP_404_NOT_FOUND)
        # check unique
        try:
            taken = Taken.objects.create(member=member, lecture=lecture)
        except:
            return Response({"message": "already taken"}, status=status.HTTP_409_CONFLICT)
        # save
        try:
            serializer = TakenSerializer(taken)
            taken.save()
            return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SyncAPI(APIView):
    permission_classes([IsAuthenticated])

    def _get_member(self, request):
        try:
            email = request.data["email"]
            member = Member.objects.get(email=email)
            return member
        except Member.DoesNotExist as e:
            return None

    def _get_lectures(self, course_serialized):
        try:
            course_id = course_serialized.data.get("id")
            lectures = Lecture.objects.filter(course_id=course_id)
            return lectures
        except:
            return None

    def _get_course(self, title, code):
        try:
            course = Course.objects.get(title=title, code=code)
            course_serialized = CourseSerializer(course)
            return course_serialized
        except Course.DoesNotExist as e:
            return None

    def post(self, request):
        try:
            member = self._get_member(request=request)
            if member is None:
                return Response({"message": "Member does not exist in DB"}, status=status.HTTP_404_NOT_FOUND)
            title = request.data["title"]
            code = request.data["code"]
            lectures = request.data["course"]
            course_serialized = self._get_course(title=title, code=code)
            if course_serialized is None:
                data = {"title": title, "code": code}
                course_serialized = CourseSerializer(data=data)
                if course_serialized.is_valid():
                    course_serialized.save()
                lecturelist = [{"lecture_name": l.get(
                    "title"), "course_id": course_serialized.data.get("id")} for l in lectures]
                lecture_serialized = LectureSerializer(
                    data=lecturelist, many=True)
                if lecture_serialized.is_valid():
                    lecture_serialized.save()
            lecture_serialized = self._get_lectures(
                course_serialized=course_serialized)
            course_id = course_serialized.data.get("id")
            for l in lectures:
                if l.get("finished") == True:
                    lecture = Lecture.objects.get(
                        lecture_name=l.get('title'), course_id=course_id)
                    Taken.objects.create(
                        member=member, lecture=lecture)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class InitializeDataAPI(APIView):
    def delete(self, request):
        Member.objects.all().delete()
        Pending.objects.all().delete()
        Lecture.objects.all().delete()
        Course.objects.all().delete()
        Taken.objects.all().delete()
        return Response({"message": "deleted"}, status=status.HTTP_200_OK)
