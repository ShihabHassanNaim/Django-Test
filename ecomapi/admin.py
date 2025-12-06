from django.contrib import admin
from .models import Sp

# Register your models here.
admin.site.register(Sp)

class SpAdmin(admin.ModelAdmin):
    list_display = ('course_name' , 'teacher_name' , 'course_duration' , 'seat')