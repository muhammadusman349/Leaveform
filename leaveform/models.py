from django.db import models

# Create your models here.


class LeaveForm(models.Model):
    STATUS_CHOICES = [
        ("REVIEW", 'Review'),
        ("APPROVE", 'Approve'),
        ("REJECT", 'Reject'),
    ]
    REASON = [
        ("SICK", 'Sick'),
        ("ANNUAL", 'Annual'),
        ("OTHER", 'Other'),
    ]

    LEAVE_TYPE = [
        ("LEAVE", 'Leave'),
        ("WFH", 'Wfh'),
    ]

    TYPE_OF_REQUEST = [
        ("FULL DAY", 'Full Day'),
        ("HALF DAY", 'Half Day'),
    ]

    start_date          = models.DateField(verbose_name="Start date")
    end_date            = models.DateField(verbose_name="End date")
    reason              = models.CharField(max_length=50, blank=True, choices=REASON)
    status              = models.CharField(max_length=50, choices=STATUS_CHOICES)
    leave_detail        = models.TextField(max_length=1000, blank=True)
    leave_type          = models.CharField(max_length=50, choices=LEAVE_TYPE)
    type_of_request     = models.CharField(max_length=50, choices=TYPE_OF_REQUEST)
    comment             = models.TextField(max_length=200,null=True,blank=True)
    

    def __str__(self):
        return (self.status)   





 