from django.db import models
from account.models import User
# Create your models here.


class LeaveForm(models.Model):
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
    
    applicant           = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    start_date          = models.DateField(verbose_name="Start date")
    end_date            = models.DateField(verbose_name="End date")
    reason              = models.CharField(max_length=50, blank=True, choices=REASON)
    status              = models.CharField(max_length=50, choices=STATUS_CHOICES)
    leave_detail        = models.TextField(max_length=1000, blank=True)
    leave_type          = models.CharField(max_length=50, choices=LEAVE_TYPE)
    type_of_request     = models.CharField(max_length=50, choices=TYPE_OF_REQUEST)
    comment             = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return (self.status)   



class TimeLog(models.Model):
    TIMELOG_STATUS_CHOICES = [
        ("APPROVE", 'Approve'),
        ("REJECT", 'Reject'),
    ]

    task_name    = models.CharField(max_length=120)
    start_date   = models.DateField(null=True,blank=True)
    end_date     = models.DateField(null=True,blank=True)
    status       = models.CharField(max_length=50,choices=TIMELOG_STATUS_CHOICES)
    comment      = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    assign_to    = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return (self.task_name)

 