from rest_framework import serializers,status
from .models import LeaveForm ,TimeLog,Comment,CommentFile,TimeLogActivity
from drf_writable_nested.serializers import WritableNestedModelSerializer

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
                "email":obj.applicant.email
                }
         
class TimeLogActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model= TimeLogActivity
        fields = (
                   'id',
                   'name',
                   'start_time',
                   'end_time',
                )
        
class TimeLogSerializer(WritableNestedModelSerializer):
    activity = TimeLogActivitySerializer(many=True,required=False)
    class Meta:
        model = TimeLog
        fields=(
                
                'task_name',
                'start_date',
                'end_date',
                'assign_to',
                'status',
                'activity',
                'comment',
                'created_at',
                'updated_at',

                )

class CommentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFile
        fields = ('id','comment','file')
class CommentSerializer(WritableNestedModelSerializer):
    commentfile = CommentFileSerializer(many=True,required=False)
    class Meta:

        model = Comment
        fields = ( 
                    'id',
                    'comment',
                    'comment_type',
                    'comment_type_id',
                    'edited',
                    'commentfile',
                    'created_by',
                    'created_at',
                    'updated_at',
                )


