from django.contrib import admin

# Register your models here.
# yourapp/admin.py
from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('usn', 'first_name', 'last_name', 'mobile_no', 'email', 'parents_contact_no', 'dob')

admin.site.register(Student, StudentAdmin)
