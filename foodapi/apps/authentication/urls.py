from django.urls import path


from .views import RegistrationAPIView, LoginAPIView, PermissionsApiView

app_name = "authentication"

urlpatterns = [
    path('users/register', RegistrationAPIView.as_view(),
         name='user_signup'),
    path('users/login', LoginAPIView.as_view(),
         name='user_login'),
    path('users/permissions', PermissionsApiView.as_view(),
         name='permissions'),
]