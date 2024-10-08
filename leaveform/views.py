from django.shortcuts import render
from rest_framework.response import Response
from .models import LeaveForm ,TimeLog,Comment
from .serializers import LeaveFormSerializer ,TimeLogSerializer,CommentSerializer
from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .filters import LeaveFormFilter
# Create your views here.


class LeaveFormView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = LeaveFormSerializer
    filterset_class   = LeaveFormFilter
    # filter_backends    = [SearchFilter]
    # search_fields      =['leave_type','type_of_request']
    # filter_backends = [OrderingFilter]
    # ordering_fields=['id',"reason","start_date","end_date"]
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
            # queryset  = LeaveForm.objects.select_related("approve_by")
            # queryset = LeaveForm.objects.prefetch_related("applicant")[:2]
            # queryset = LeaveForm.objects.distinct("applicant")
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
            queryset  = TimeLog.objects.filter(assign_to__id=self.request.user.id)
        return queryset 

    def post(self, request, *args, **kwargs):
        # print("data",self.request.user)

        request.data['assign_to']=self.request.user.id
        serializer = TimeLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
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
        
    def get_queryset(self, *args, **kwargs):
        if 'id' not in kwargs:
            comment_type = self.request.query_params.get('comment_type',None)
            comment_type_id = self.request.query_params.get('comment_type_id',None)
            self.queryset = Comment.objects.filter(comment_type=comment_type,comment_type_id=comment_type_id)
        return self.queryset
     
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save(created_by= self.request.user) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    