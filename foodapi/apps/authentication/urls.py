from django.urls import path


from .views import RolesAPIView, LoginAPIView

app_name = "authentication"

urlpatterns = [
    path('users/register', RolesAPIView.as_view(),
         name='user_signup'),
    path('users/login', LoginAPIView.as_view(),
         name='user_login'),
]