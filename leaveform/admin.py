from django.contrib import admin
from .models import LeaveForm ,TimeLog,Comment,CommentFile
# Register your models here.

admin.site.register(LeaveForm)
admin.site.register(TimeLog)
admin.site.register(Comment)
admin.site.register(CommentFile)
