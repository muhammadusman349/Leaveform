from account.models import User,OtpVerify,Organization,Department
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers,status
import pyotp
import base64
import random
import string
import time
from datetime import datetime
from django.utils import timezone

#A class state cannot be accessed or modified by a static method.
#The static method does not accept any specific parameter.
#static method cannot access the class or instance data,they cannot modify the class state.
#static method cannot change the behavior or affect a class
#static method does not depend on the state of an instance or class
class generateKey:
    @staticmethod
    def return_value(user_obj):
        timestamp = str(int(time.time()))
        user_id = str(user_obj.id)
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return timestamp + user_id + random_string
    
class UserListSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    
    class Meta:
        model = User
        fields=(
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'date_of_joining',
            'employee_id',
            'department',
            'organization',
            'password',
            'password2',
            'created_at',
            'updated_at',
            )
        read_only_fields=["created_at","updated_at"]
        extra_kwargs = { 
                        'password': {'write_only': True},

                        'organization':{'required':False}
                        } 


class Registrationserializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    
    class Meta:
        model = User
        fields=(
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'date_of_joining',
            'employee_id',
            'department',
            'organization',
            'password',
            'password2',
            'created_at',
            'updated_at',
            )
        read_only_fields=["created_at","updated_at"]
        extra_kwargs = { 
                        'password': {'write_only': True},

                        'organization':{'required':False}
                        } 
                        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})
        return attrs
    
    def create(self,validated_data):   
        user_obj = User(
            first_name      = validated_data.get('first_name'),
            last_name       = validated_data.get('last_name'),
            phone           = validated_data.get('phone'),
            email           = validated_data.get('email'),
            department      = validated_data.get('department'),
            organization    = validated_data.get('organization'),
            date_of_joining = validated_data.get('date_of_joining'),
            employee_id     = validated_data.get('employee_id'))  
                  
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj
    
    
class Loginserializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password  =serializers.CharField(required=True)
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "provided credentials are not valid/email"}, code=status.HTTP_401_UNAUTHORIZED)

        if user:
            if not user.check_password(password):
                raise serializers.ValidationError(
                    {"password": "provided credentials are not valid/password"}, code=status.HTTP_401_UNAUTHORIZED)
                
        # if not user:
        #     raise serializers.ValidationError(
        #         {"email": "User not found"}, code=status.HTTP_401_UNAUTHORIZED)


        token = RefreshToken.for_user(user)

        attrs['id']            = int(user.id)
        attrs['first_name']    = str(user.first_name)
        attrs['last_name']     = str(user.last_name)
        attrs['organization']  = (user.organization.id) 
        attrs['is_owner']      = str(user.is_owner)
        attrs['phone']         = str(user.phone)
        attrs['email']         = str(user.email)
        attrs['access_token']  = str(token.access_token)
        attrs['refresh_token'] = str(token)
        
        return attrs

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get("new_password", None)
        old_password = attrs.get("old_password", None)
        try:
            user = User.objects.get(email=str(self.context['user']))
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"error ": "User not found."})
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {"error": "Incorrect Password"})
        if new_password and len(new_password) > 5:
            if user.check_password(new_password):
                raise serializers.ValidationError(
                    {"error": "New password should not be same as old_password"})
        else:
            raise serializers.ValidationError(
                {"error": "Minimum length of new Password should be greater than 5"})
        return attrs

    def create(self, validated_data):    
        user = self.context['user']
        user.set_password(validated_data.get("new_password"))
        user.save()
        return validated_data
    


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    def validate(self, attrs):
        email = attrs.get("email", None)
        if email is not None:
            try:
                userObj = User.objects.get(email__iexact=email)
                otp_obj = OtpVerify.objects.filter(user__id=userObj.id).first()
                if otp_obj:
                    otp_obj.delete()
                key = base64.b32encode(generateKey.return_value(userObj).encode())  
                otp_key = pyotp.TOTP(key)  
                otp = otp_key.at(6)
                otp_obj = OtpVerify()
                otp_obj.user = userObj
                otp_obj.otp = otp
                otp_obj.save()
                
            except Exception as e:
                print("Exception", e) 
                raise serializers.ValidationError(
                    {"email": "Valid email is Required"})
        else:
            raise serializers.ValidationError({"email": "email is required"})
        return attrs

class ResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        otp = attrs.get("otp", None)
        password = attrs.get("password", None)
        if otp:
            try:
                otpobj = OtpVerify.objects.filter(otp=otp).first()
                if otpobj:
                    otpobj.user.set_password(password)
                    otpobj.delete()
                    otpobj.user.save()
                else:
                    raise OtpVerify.DoesNotExist
            except OtpVerify.DoesNotExist:
                raise serializers.ValidationError(
                    {"error": "Valid OTP  is Required"})
        else:
            raise serializers.ValidationError({"error": "email is required"})
        return attrs



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields =["id","manager","name" ,"created_at", "updated_at"] 
        read_only_fields = ["id","created_at", "updated_at"]
        

