from django.contrib import admin
from .models import EmployeeProfile
from Employee.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):

        list_display=['user','designation','salary','Currency', 'working_days','pub_date']
        list_filter=['pub_date','designation','working_days']

        class Meta:
            abstract=True;
        def __str__(self):
            return self.user

class EmployeeAdmin(ProfileAdmin,ImportExportModelAdmin):
    pass

admin.site.register(EmployeeProfile,EmployeeAdmin)
