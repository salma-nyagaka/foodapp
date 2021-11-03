from django.urls import path


from .views import RoleAPIView, LoginAPIView

app_name = "authentication"

urlpatterns = [
    path('users/register', RoleAPIView.as_view(),
         name='user_signup'),
    path('users/login', LoginAPIView.as_view(),
         name='user_login'),
]