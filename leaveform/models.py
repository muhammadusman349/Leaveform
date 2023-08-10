from django.db import models
from account.models import User
from .__init__ import REASON ,LEAVE_TYPE,TYPE_OF_REQUEST,STATUS_CHOICES,TIMELOG_STATUS_CHOICES,COMMENT_TYPE_CHOICE
# Create your models here.


class LeaveForm(models.Model):

    applicant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="applicant")
    reason = models.CharField(max_length=50, blank=True, choices=REASON)
    leave_detail = models.TextField(max_length=1000, blank=True)
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPE)
    type_of_request = models.CharField(max_length=50, choices=TYPE_OF_REQUEST)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    approve_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="approve_by")
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return (self.status)   
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver

@receiver(pre_save,sender=LeaveForm)
def leave_pre_save_receiver(sender, instance, *args,**kwargs):
    print(instance.leave_type ,instance.id)


@receiver(post_save,sender=LeaveForm)
def leave_post_save_receiver(sender,instance,created, **kwargs):
        if created:
            print("send leave",instance.leave_type)
            instance.save()
        else:
            print(instance.leave_type, 'just saved')
            print("LEAVEFORM OBJECT CREATED")
            print(sender,instance,kwargs)

@receiver(pre_delete,sender=LeaveForm)
def leave_pre_delete_receiver(sender, instance, *args,**kwargs):
    print(instance.id,'Will Be Removed')


@receiver(post_delete,sender=LeaveForm)
def leave_post_delete_receiver(sender,instance, **kwargs):
   
    print(instance.id,'Has Removed')
     

class TimeLog(models.Model):
    
    task_name = models.CharField(max_length=120)
    status = models.CharField(max_length=50,choices=TIMELOG_STATUS_CHOICES)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assign_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return (self.task_name)

class TimeLogActivity(models.Model):
    timelog = models.ForeignKey(TimeLog, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=120)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.name)

class Comment(models.Model):
    comment = models.TextField()
    comment_type = models.CharField(max_length=120,choices=COMMENT_TYPE_CHOICE)
    comment_type_id = models.IntegerField(unique= True)
    edited = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
   
    def __str__(self):
        return str(self.created_by)
    
class CommentFile(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Email")
    file    = models.FileField(upload_to='Comment_File/',null=True,blank=True)

    def __str__(self):
        return str(self.comment)
