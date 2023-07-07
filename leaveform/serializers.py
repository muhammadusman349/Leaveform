from rest_framework import serializers,status
from .models import LeaveForm ,TimeLog

class LeaveFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveForm
        fields=(
            'applicant',
            'start_date',
            'end_date',
            'reason',
            'status',
            'leave_detail',
            'leave_type',
            'type_of_request',
            'comment',
            'created_at',
            'updated_at',
            )


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

