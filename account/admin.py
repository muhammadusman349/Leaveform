from django.contrib import admin
from .models import User,OtpVerify,Organization,Department
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ("id","email")
    list_filter=["date_of_joining","department","organization"]
    raw_id_fields = ("person",)
    list_display = ("id",'first_name', 'last_name','email','department', 'organization', "is_verified","is_approved",'date_of_joining')
class DepartmentAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display= ("id","name","manager")
class OrganizationAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display= ("id","name","email","address","phone")

admin.site.register(User,UserAdmin)
admin.site.register(OtpVerify)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Department,DepartmentAdmin)

