from django.shortcuts import render
from rest_framework.response import Response

from .models import LeaveForm ,TimeLog,Comment
from .serializers import LeaveFormSerializer ,TimeLogSerializer,CommentSerializer
from rest_framework import generics, permissions, status
# Create your views here.


class LeaveFormView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = LeaveFormSerializer
    queryset           = LeaveForm.objects.all()
    lookup_field       = 'id'
    

    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            instance = LeaveForm.objects.get(id=self.kwargs['id'])
            serializer = self.get_serializer(instance)
            # print("..........>>>>>>>instance<<<<<<<<<<.........",serializer.data)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)
        
    def get_queryset(self):
        queryset = self.queryset
        if 'id' not in self.kwargs:
            queryset  = LeaveForm.objects.filter(applicant__id = self.request.user.id)
        return queryset 
        
    def post(self, request, *args, **kwargs):
            serializer = LeaveFormSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(applicant= self.request.user) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
 
        # instance = LeaveForm.objects.get(id=self.kwargs["id"])
        # serializer = LeaveFormSerializer(instance,data = request.data)
        # if serializer.is_valid():
        #     user=self.request.user
        #     print("user......",user)
        #     leave_obj= serializer.save()
        #     if leave_obj.status == "Approve":
        #         leave_obj.approve_by=user
        #         leave_obj.save()
        #         print("leave_obj....",leave_obj)
        #     return Response(serializer.data,status=status.HTTP_200_OK)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class TimeLogView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = TimeLogSerializer
    queryset           = TimeLog.objects.all()
    lookup_field       = 'id'
    

    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
    
    def get_queryset(self):

        queryset = self.queryset
        if 'id' not in self.kwargs:
            queryset  = LeaveForm.objects.filter(applicant__organization__id = self.request.user.organization.id)

        return queryset 

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class CommentView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = CommentSerializer
    queryset           = Comment.objects.all()
    lookup_field       = 'id'
    

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
    