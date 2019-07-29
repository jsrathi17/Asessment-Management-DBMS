from django.db import models
#from multiselectfield import MultiSelectField
from django.utils import timezone
import datetime

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


Department = (
    ('BEX', 'BEX'),
    ('BCT', 'BCT'),
    ('BCE', 'BCE'),
    ('BME', 'BME'),
    ('BAE', 'BAE'),
    ('BEL', 'BEL'),
)

class Room(models.Model):
	room_id = models.AutoField(primary_key=True)
	capacity = models.IntegerField(null=True)
	building_name = models.CharField(max_length=200)	



	def __init__(self):
		return room_id
		

class Department(models.Model):
	deparment_id = models.AutoField(primary_key=True)
	#building_name = models.ForeignKey(Room,on_delete = models.CASCADE,default=None)
	name = models.CharField(max_length=200,choices=Department,default='BEX')

	def __str__(self):
		return self.name

class Course(models.Model):
	course_id = models.AutoField(primary_key=True)
	#course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
	course_subject = models.CharField(max_length=200)
	#department_id = models.ForeignKey(Department, on_delete=models.CASCADE,default=None)
	

	def __str__(self):
		return self.course_subject



class Assesment(models.Model):
	assesment_id = models.AutoField(primary_key=True)
	course_id = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
	assesment_date = models.DateField()
	start_time = models.TimeField(null=True,help_text="24hrs format hh:mm:ss")
	duration = models.TimeField(null=True,help_text="hh:mm")
	full_marks = models.IntegerField(default=20)
	pass_marks = models.IntegerField(default=8)
	#assesment_day = models.CharField(max_length=200, choices = DAYS_OF_WEEK, default='Sunday')
	#room_id = models.ForeignKey(Room,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.assesment_id

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	course_id = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
	teacher_name = models.CharField(max_length=200)
	department_id = models.ForeignKey(Department,on_delete=models.CASCADE,default=None)
	

	def __str__(self):
		return self.teacher_name

