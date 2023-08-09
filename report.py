import os
import django

import django
from openpyxl import Workbook
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from account.models import *
from leaveform.models import *

wb= Workbook()
ws = wb.active


header = (['id',"first name","last name","email","employee id","date of joining","phone","department",
           "organization","is approved","is superuser","is verified","is active","is staff","is owner","created at"])
ws.append(header)

users = User.objects.all()
for user in users:
    # print(user)
    data_list=[ 
        user.id,
        user.first_name,
        user.last_name,
        user.email,
        user.employee_id,
        user.date_of_joining,
        user.phone,
        user.department.name,
        user.organization.name,
        user.is_approved,
        user.is_superuser,
        user.is_verified,
        user.is_active,
        user.is_staff,
        user.is_owner,
        str(user.created_at)
        ]
    ws.append(data_list)
    # print(data_list)
path = 'C:/Users/Usman/Downloads/Api/User_Report.xlsx'
wb.save(path)
wb.close()

