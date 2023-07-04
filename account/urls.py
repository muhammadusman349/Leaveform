from django.urls import path
from .views import RegistrationApi,LoginApiView,LogoutAPIView,ChangePasswordView,ForgetPasswordView,ResetPasswordView,OrganziationView,DepartmentView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path("register/",                   RegistrationApi.as_view(),              name='register'),
    path("login/",                      LoginApiView.as_view(),                 name='login'),
    path('logout/',                     LogoutAPIView.as_view(),                name='logout'),
    path('token-refresh/',              jwt_views.TokenRefreshView.as_view(),   name='token_refresh'),
    path('changepassword/',             ChangePasswordView.as_view(),           name='change-password'),
    path('forget/password/',            ForgetPasswordView.as_view(),           name='forget-password'),
    path('reset/password/',             ResetPasswordView.as_view(),            name='reset-password'),
    path('department/',                 DepartmentView.as_view(),               name='department-listcreate-view'),
    path('department/<int:id>/',        DepartmentView.as_view(),               name='department-detail-view'),
    path('organziation/',               OrganziationView.as_view(),             name='organziation-listcreate-view'),
    path('organziation/<int:id>/',      OrganziationView.as_view(),             name='organziation-detail-view'),
]