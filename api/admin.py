from django.contrib import admin
from api.models import Course, Lecture, Member, Pending, Taken, Team

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Taken)
admin.site.register(Lecture)
admin.site.register(Course)
admin.site.register(Pending)
