from django.contrib import admin
from .models import User,OtpVerify,Organization,Department

# Register your models here.

admin.site.register(User)
admin.site.register(OtpVerify)
admin.site.register(Organization)
admin.site.register(Department)

