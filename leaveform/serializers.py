from rest_framework import serializers,status
from .models import LeaveForm ,TimeLog,Comment

class LeaveFormSerializer(serializers.ModelSerializer):
    applicant = serializers.SerializerMethodField()
    class Meta:
        model = LeaveForm
        fields=(
            'id',
            'applicant',
            'start_date',
            'end_date',
            'reason',
            'status',
            'leave_detail',
            'leave_type',
            'type_of_request',
            'comment',
            'approve_by',
            'created_at',
            'updated_at',
            )
    def get_applicant(self,obj):
        return {
                "id": obj.applicant.id,
                "first_name":obj.applicant.first_name,
                "last_name":obj.applicant.last_name,
                "email":obj.applicant.email,
                }
         

class TimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields=(
                
                'task_name',
                'start_date',
                'end_date',
                'assign_to',
                'status',
                'comment',
                'created_at',
                'updated_at',
                
                )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (  'id',
                    'comment_id',
                    'comment_type',
                    'edited',
                    'created_by',
                    'created_at',
                    'updated_at',
                 )

