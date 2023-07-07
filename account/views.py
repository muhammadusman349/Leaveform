from rest_framework import status,generics
from rest_framework.response import Response
from account.serializers import (
                                 Registrationserializer,
                                 Loginserializer,
                                 ChangePasswordSerializer,
                                 ForgetPasswordSerializer,
                                 ResetPasswordSerializer,
                                 DepartmentSerializer)
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import permissions
from django.shortcuts import render
from .models import Department,User


class RegistrationApi(generics.GenericAPIView):
    permission_classes      = [permissions.IsAuthenticated]
    serializer_class        = Registrationserializer
    queryset                = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = Registrationserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.organization=self.request.user.organization
            user.employee_id = str(user.id)
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
            return Response({'password': ' password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ForgetPasswordView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'opt': 'successfully send OTP '}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ResetPasswordView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'password': 'successfully set New Password'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
class DepartmentView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
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