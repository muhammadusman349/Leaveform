import os
import django
import datetime
import django
from openpyxl import Workbook
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from account.models import *
from leaveform.models import *

wb= Workbook()
ws = wb.active

Header = (['id','Manager','Name','Created At'])
ws.append(Header)
departments = Department.objects.all()
for department in departments:
    data_list = [
        department.id,
        department.manager.email,
        department.name,
        str(department.created_at),
    ]
    ws.append(data_list)

wb.save('Department_Report.xlsx')

