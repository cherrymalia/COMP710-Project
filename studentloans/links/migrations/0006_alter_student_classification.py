# Generated by Django 5.1 on 2024-04-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_alter_student_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classification',
            field=models.CharField(choices=[('SR', 'Senior'), ('GR', 'Graduate'), ('FR', 'Freshman'), ('NE', 'Not Enrolled'), ('JR', 'Junior'), ('SO', 'Sophomore')], max_length=2),
        ),
    ]
