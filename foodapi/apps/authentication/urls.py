from django.urls import path


from .views import RoleAPIView, LoginAPIView

# app_name = "authentication"

urlpatterns = [
     path('register', RoleAPIView.as_view(), name='user_registration'),
     path('login', LoginAPIView.as_view(), name='user_login'),
]
