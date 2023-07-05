from django.shortcuts import render
from .models import LeaveForm ,TimeLog
from .serializers import LeaveFormSerializer ,TimeLogSerializer
from rest_framework import generics, permissions, status
# Create your views here.


class LeaveFormView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = LeaveFormSerializer
    queryset = LeaveForm.objects.all()
    lookup_field = 'id'
    

   
    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class TimeLogView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = TimeLogSerializer
    queryset = TimeLog.objects.all()
    lookup_field = 'id'
    

    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
