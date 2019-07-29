from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Register your models here.




admin.site.site_header='Assesment Management System'
admin.site.register(Assesment)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Teacher)
admin.site.index_title = "Assesment\' database"
