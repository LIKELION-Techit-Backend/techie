# Generated by Django 5.0 on 2023-12-16 22:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_alter_member_email_alter_member_password"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="course_name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="course",
            name="course_count",
        ),
    ]