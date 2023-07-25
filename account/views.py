from rest_framework import status,generics
from rest_framework.response import Response
from account.serializers import (
                                 Registrationserializer,
                                 Loginserializer,
                                 ChangePasswordSerializer,
                                 ForgetPasswordSerializer,
                                 ResetPasswordSerializer,
                                 DepartmentSerializer,
                                 UserListSerializer,
                                 )
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import permissions
from django.shortcuts import render
from .models import Department,User
from .filters import UserFilter,DepartmentFilter
class UserView(generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticated]
    serializer_class        = UserListSerializer
    filterset_class         = UserFilter
    queryset                = User.objects.all()
    lookup_field            = 'id'
  
    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
    def get_queryset(self):
        queryset = self.queryset
        if 'id' not in self.kwargs:
            # queryset = User.objects.only("date_of_joining")
            # queryset = User.objects.defer("department","date_of_joining")
            # queryset = User.objects.values_list("first_name","last_name","email",named=True)
            # queryset = User.objects.exclude(id=3)
            # queryset = User.objects.values("id","first_name","last_name","email")
            # queryset = User.objects.exclude(id=self.request.user.id)
            # queryset = User.objects.alias()
            # queryset = User.objects.check("first_name")
            # queryset = User.objects.select_related('department')[:3]
            # queryset = User.objects.prefetch_related("department")[:2]
            # queryset = User.objects.distinct("first_name")
            # queryset = User.objects.select_related("organization").prefetch_related("department")
            # queryset = User.objects.prefetch_related('department')
            # queryset = User.objects.filter(organization__id=self.request.user.organization.id).exclude(id=self.request.user.id)
            # queryset = User.objects.aggregate(Sum('employee_id'))
            queryset = User.objects.aggregate("")
        return queryset
    # "😃", "👏" ,"👇" #
class UserApproveView(generics.GenericAPIView):
    permission_classes      = [permissions.IsAuthenticated]  
    def post(self,request,*args,**kwargs):
        try:
            id=self.request.query_params.get('id',None)
            user=User.objects.get(id=id)
            user.is_verified=True
            user.is_approved = True
            user.save()
            return Response({"Message":"User is approve 😃"},status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Error":"User is Not Exist 👏"},status=status.HTTP_400_BAD_REQUEST)    

class RegistrationApi(generics.GenericAPIView):
    permission_classes      = [permissions.IsAuthenticated]
    serializer_class        = Registrationserializer
    queryset                = User.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if 'id' not in self.kwargs:
            queryset= User.objects.filter(organization__id=self.request.user.organization.id)
        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = Registrationserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.organization=self.request.user.organization
            user.employee_id = str(user.id)
            user.is_active = True
            user.save()
            return Response(serializer.data,status=status.HTTP_200_OK)       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginApiView(generics.GenericAPIView): 
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = Loginserializer
    
    
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": self.request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={
                                           'user': self.request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'password': ' password changed successfully 😃'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ForgetPasswordView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'opt': 'successfully send OTP 😃'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ResetPasswordView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'password': 'successfully set New Password 😃'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
class DepartmentView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
    filterset_class  = DepartmentFilter
    queryset = Department.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if 'id' not in self.kwargs:
            queryset = Department.objects.filter(manager__organization__id=self.request.user.organization.id)
        return queryset


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)