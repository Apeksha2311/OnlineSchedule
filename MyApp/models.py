from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
   

class Course(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')

    def __str__(self):
        return self.name

class Lecture(models.Model):
    date = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course} by {self.instructor}'