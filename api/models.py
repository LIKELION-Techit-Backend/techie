from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=20, null=False)
    role = models.CharField(max_length=10, null=False, default="member")
    team = models.ForeignKey(
        'Team', related_name='team', on_delete=models.CASCADE, db_column="team_id", null=True)


class Pending(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey(
        'Member', related_name='pending_member', on_delete=models.CASCADE, db_column="member_id")
    team = models.ForeignKey(
        'Team', related_name='pending_team', on_delete=models.CASCADE, db_column="team_id")


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    abbreviation = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=30, unique=True, blank=True)


class Lecture(models.Model):
    id = models.BigAutoField(primary_key=True)
    lecture_name = models.CharField(max_length=100)
    course_id = models.ForeignKey(
        'Course', related_name='course', on_delete=models.CASCADE, db_column="course_id")


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=64, unique=True)


class Taken(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey(
        'Member', related_name='member', on_delete=models.CASCADE, db_column="member_id")
    lecture = models.ForeignKey(
        'Lecture', related_name='lecture', on_delete=models.CASCADE, db_column="lecture_id")

    class Meta:
        unique_together = ['member', 'lecture']
