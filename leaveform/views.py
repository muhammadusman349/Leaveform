from django.shortcuts import render
from .models import LeaveForm
from .serializers import LeaveFormSerializer
from rest_framework import generics, permissions, status
# Create your views here.


class LeaveFormView(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class = LeaveFormSerializer
    queryset = LeaveForm.objects.all()
    lookup_field = 'id'
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class LeaveFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = LeaveFormSerializer
    queryset = LeaveForm.objects.all()
    lookup_field = 'id'
    

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

