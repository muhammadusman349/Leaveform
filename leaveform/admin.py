from django.contrib import admin
from .models import LeaveForm ,TimeLog,Comment,CommentFile,TimeLogActivity
# Register your models here.

class LeaveFormAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=("id","leave_type","type_of_request","reason","status","created_at")
    search_fields = ["id","applicant"]

class TimeLogAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id","task_name","status","assign_to","start_date"]
class CommentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=("id","comment_type","edited","created_by")

admin.site.register(LeaveForm,LeaveFormAdmin)
admin.site.register(TimeLog,TimeLogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(CommentFile)
admin.site.register(TimeLogActivity)
