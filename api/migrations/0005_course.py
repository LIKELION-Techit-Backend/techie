# Generated by Django 5.0 on 2023-12-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_member_email_member_password_alter_member_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=30)),
                ("course_count", models.IntegerField(default=0)),
            ],
        ),
    ]
