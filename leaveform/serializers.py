from rest_framework import serializers,status
from .models import LeaveForm

class LeaveFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveForm
        fields=('start_date','end_date','reason','status','leave_detail','leave_type','type_of_request','comment')

