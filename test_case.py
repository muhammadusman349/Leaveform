import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from account.models import *
from leaveform.models import *
from django.db.models import *

# try:
#     obj = User.objects.get(first_name='j',last_name='Usman')
# except User.DoesNotExist:
    # print('error:')
    # obj = User(first_name='M',last_name='Khan',email='mkhan@hotmail.in')
    # obj.save()

# Obj = User.objects.all()
# for i in Obj:
#     if i
    
# user,created = User.objects.get_or_create(first_name='Ali',
#                                           last_name='Hamza',
#                                           email="alihamza@gmail.com",
#                                           employee_id=6,
#                                           password='alihamza123',
                                        #   date_of_joining = 2023-8-3,
#                                           department = {id=1},
#                                           organizationid = 1,
#                                           is_approved= True
#                                           )
# print(user)

# leave, created = LeaveForm.objects.get_or_create( applicant__id = "3",
#                                                  reason = 'Sick',
#                                                  leave_type= 'Leave',
#                                                  leave_detail = 'leave from home',
#                                                  type_of_request = 'Full Day',
#                                                  status = 'Approve',
#                                                  approve_by__id = 1,
#                                                  start_date = "2023-8-18",
#                                                  end_date = "2023-8-28"
     



# )

leave, created = LeaveForm.objects.get_or_create(
    # applicant__id=,
    defaults={
        'reason': "Sick",
        'leave_type': "Leave",
        'leave_detail':'leave from home',
        'type_of_request':'Full Day',
        'status':'Approve',
        # 'approve_by' : 1,
        'start_date' : "2023-8-18",
        'end_date' : "2023-8-28"
    }
)


print (leave,created)
# user = User.objects.get(id=41).delete()
# user.delete()



# queryset1 = User.objects.filter(last_name__iexact='Usman')
# print(' Queryset 1 👍:',queryset1)

# queryset2 =  Department.objects.filter(manager__email__icontains = "m")
# print("Queryset 2  👍:",queryset2)

# queryset3 = Department.objects.filter(created_at="2023-07-26T09:41:44.904752Z",)
# print("Queryset 3  👍:",queryset3)

# queryset4 = Department.objects.exclude(name = 'Front-End')
# print('Queryset 4  👍:',queryset4)

# queryset5 = User.objects.filter(department__name__in =  ['IT','BS-CS'])
# print('Queryset 5  👍:',queryset5)

# queryset6 = User.objects.exclude(department__name = 'IT')
# print('Queryset 6  👍:',queryset6)

# queryset7 = User.objects.filter(email__endswith = ".com")
# print("Queryst 7   👍:",queryset7)

# queryset8 = User.objects.exclude(organization__address="	Rawalpindi")
# print('Queryset 8  👍:',queryset8)

# queryset9 = User.objects.values_list("first_name","last_name","email")
# print('Queryset 9  👍:',queryset9)

# queryset10 = Department.objects.filter(manager__first_name='M')
# print('Queryset 10 👍:',queryset10)

# queryset11 = LeaveForm.objects.filter( end_date='2023-07-26')
# print('Queryset 11 👍:',queryset11)

# queryset12 = LeaveForm.objects.exclude(reason = 'Sick')
# print('Queryset 12 👍: ',queryset12.count())

# queryset13 =LeaveForm.objects.values("applicant","reason","leave_detail")
# print("Queryset 13 👍:",queryset13)

# queryset14 = LeaveForm.objects.filter(approve_by__first_name='M')
# print("Queryset 14 👍:",queryset14)

# queryset15 = User.objects.values("email")
# print("Queryset 15 👍:",queryset15)

# ar = User.objects.filter(first_name="M")
# print(ar.count())

# Leave = LeaveForm.objects.only('reason')
# for i in Leave:
#     print("reason only",i.reason)

# queryset16 = Department.objects.defer("name")
# for q in queryset16:
    # print("Queryset 16 👍:",q.manager,q.created_at)

# queryset= LeaveForm.objects.defer("status")
# for i in queryset:
    # print("defer",i.type_of_request)

# queryset = TimeLog.objects.filter(assign_to__first_name="Guf")
# for i in queryset:
    # print("queryset",i.assign_to.first_name)

# department = Department.objects.all().values("name")
# for j in department:
    # print("department",j)


# q= User.objects.aggregate(Min('employee_id'))
# print(q)

# anno = User.objects.values('first_name').annotate(Count('id'))
# print(anno)

# dep = User.objects.values('department').annotate(Count('department'))
# print(dep)

# queryset1 = TimeLog.objects.filter(assign_to__first_name="Guf")
# for i in queryset1:
#     print("queryset",i.assign_to.last_name)

# querset = LeaveForm.objects.filter(leave_type='Leave')
# print(querset)

# annotatedOutput = User.objects.aggregate(Count('first_name'))
# for f in annotatedOutput:
# print(annotatedOutput)

# another = User.objects.filter(first_name__startswith='M').aggregate(Sum("id"))
# print(another)

# user = User.objects.aggregate(Min('id'))
# print(user)

# distinct  = LeaveForm.objects.distinct("reason")

# print("distinct",distinct)

# reason = LeaveForm.objects.values_list('reason',flat=True) #.distinct()
# print(reason)



# queryset= LeaveForm.objects.all().values('reason') #.distinct()
# print(queryset)

# queryset = LeaveForm.objects.all().

# user = User.objects.filter(is_verified = True)
# for i in user:
#     print("verify:",i)

# defer = User.objects.defer("first_name")
# for i in defer:
#     print("defer",i.email)
    
# leave = LeaveForm.objects.defer("status","reason")
# print(leave)
# for i in leave:
#     print("status",i)

# queryset17 = User.objects.filter(is_verified=False)
# print('Queryset 17 👍:',queryset17)

# queryset18 = LeaveForm.objects.values_list()
# print("Queryset 18 👍:",queryset18)

# queryset19 = LeaveForm.objects.values("leave_detail")
# print("Queryset 19 👍:",queryset19)

# queryset20 = LeaveForm.objects.filter()
# print("Queryset 20 👍:",queryset20)




# queryset = User.objects.filter(department__name__in=['IT','SE','BS-SE','BS-CS'])
# queryset = User.objects.filter(last_name="usman")
# queryset = User.objects.exclude(department__name  = 'IT')
# queryset = User.objects.filter(last_name__icontains = "man")
# queryset = User.objects.filter(first_name__startswith = 'a')
# queryset = User.objects.filter(email__endswith = ".com")
# queryset = User.objects.all()
# queryset = User.objects.only("employee_id")
# queryset = User.objects.defer("department","date_of_joining")
# queryset = User.objects.values_list("first_name","last_name","email",flat=True)
# queryset = User.objects.exclude(id=3)
# queryset = User.objects.values("id","first_name","last_name","email")
# queryset = User.objects.select_related('department')[:3]
# queryset = User.objects.prefetch_related("department")[:2]
# queryset = User.objects.distinct("first_name")
# queryset = User.objects.select_related("organization").prefetch_related("department")
# queryset = User.objects.prefetch_related('department')
# queryset = User.objects.filter(organization__id=self.request.user.organization.id).exclude(id=self.request.user.id)
# print(queryset.count())
# print(queryset.exists())
# queryset = User.objects.values_list('id','last_name',named=True)
# queryset = User.objects.values("first_name","last_name")
# queryset = User.objects.values_list("email","date_of_joining")
# queryset = User.objects.values("id","department","organization")
# queryset = User.objects.all()[3:10]

# queryset = User.objects.exclude(last_name__endswith ='i')
# queryset = Department.objects.all().count()
# leave = Organization.objects.all().count()
# queryset = User.objects.filter(first_name__startswith='m') & User.objects.filter(last_name__startswith='U')
# queryset = User.objects.filter(Q(first_name__startswith='m')& Q(last_name__startswith='g'))
# queryset = User.objects.filter(id=1)
# queryset =User.objects.select_related('department').all()

# print(queryset,leave)
# queryset1 = TimeLog.objects.all().count()

# print('Logtime.....',queryset1)