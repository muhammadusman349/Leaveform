from django.contrib import admin
from .models import LeaveForm ,TimeLog,Comment,CommentFile,TimeLogActivity
# Register your models here.

class LeaveFormAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=("id","leave_type","type_of_request","reason","status","applicant","approve_by","created_at")
    search_fields = ["applicant__first_name"]
    list_filter = ["leave_type","type_of_request","status","reason"]

class TimeLogAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id","task_name","status","assign_to","start_date"]
    list_filter = ["status","assign_to"]

class TimeLogActivityAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=("id","name","timelog","start_time","end_time")

class CommentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display=("id","comment_type","comment_type_id","edited","created_by")
    list_filter=["comment_type_id","created_by"]

class CommentFileAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ("id","comment","file")    



admin.site.register(LeaveForm,LeaveFormAdmin)
admin.site.register(TimeLog,TimeLogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(CommentFile,CommentFileAdmin)
admin.site.register(TimeLogActivity,TimeLogActivityAdmin)
