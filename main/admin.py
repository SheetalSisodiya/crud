from django.contrib import admin
from main .models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','course','date']

admin.site.register(StudentModel, StudentAdmin)
