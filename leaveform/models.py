from django.db import models
from account.models import User
# Create your models here.

STATUS_CHOICES = [
        ("Review", 'Review'),
        ("Approve", 'Approve'),
        ("Reject", 'Reject'),
    ]
REASON = [
        ("Sick", 'Sick'),
        ("Annual", 'Annual'),
        ("Other", 'Other'),
    ]

LEAVE_TYPE = [
        ("Leave", 'Leave'),
        ("Wfh", 'Wfh'),
    ]

TYPE_OF_REQUEST = [
        ("Full Day", 'Full Day'),
        ("Half Day", 'Half Day'),
    ]


class LeaveForm(models.Model):

    applicant           = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="applicant")
    reason              = models.CharField(max_length=50, blank=True, choices=REASON)
    leave_detail        = models.TextField(max_length=1000, blank=True)
    leave_type          = models.CharField(max_length=50, choices=LEAVE_TYPE)
    type_of_request     = models.CharField(max_length=50, choices=TYPE_OF_REQUEST)
    status              = models.CharField(max_length=50, choices=STATUS_CHOICES)
    comment             = models.TextField()
    approve_by          = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="approve_by")
    start_date          = models.DateField(verbose_name="Start date")
    end_date            = models.DateField(verbose_name="End date")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return (self.status)   


TIMELOG_STATUS_CHOICES = [
        ("Approve", 'Approve'),
        ("Reject", 'Reject'),
    ]
class TimeLog(models.Model):
    
    task_name    = models.CharField(max_length=120)
    status       = models.CharField(max_length=50,choices=TIMELOG_STATUS_CHOICES)
    comment      = models.TextField()
    start_date   = models.DateField(null=True,blank=True)
    end_date     = models.DateField(null=True,blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    assign_to    = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return (self.task_name)

 