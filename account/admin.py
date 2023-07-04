from django.contrib import admin
from .models import User,OtpVerify,Organziation,Department

# Register your models here.

admin.site.register(User)
admin.site.register(OtpVerify)
admin.site.register(Organziation)
admin.site.register(Department)

