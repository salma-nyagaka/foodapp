from django.urls import path


from .views import RoleAPIView, LoginAPIView, AllUsersAPIView, SingleUserAPIView


urlpatterns = [
     path('register', RoleAPIView.as_view(), name='user_registration'),
     path('login', LoginAPIView.as_view(), name='user_login'),
     path('details', AllUsersAPIView.as_view(), name='all_users'),
     path('details/<str:user_id>', SingleUserAPIView.as_view(), name='single_user'),
]
