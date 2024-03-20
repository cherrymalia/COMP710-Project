from django.db import models

class UserAccount(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    email = models.EmailField()

    class Meta:
        abstract = True

class Student(UserAccount):
    YEAR_IN_SCHOOL = {
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
        ("NE", "Not Enrolled")
    }
    classification = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL)
    associated_parent = models.IntegerField(null = True, blank = True) # user ID of student's parent (if applicable)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class Parent(UserAccount):
    associated_student = models.IntegerField(null = True, blank = True) # user ID of parent's child (if applicable)

    def __str__(self):
        return f'Parent: {self.first_name} {self.last_name}'