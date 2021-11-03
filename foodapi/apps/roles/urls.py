from django.urls import path


from .views import RoleAPIView, SingleRoleAPIView, AllRolesPIView


urlpatterns = [
    path('register', RoleAPIView.as_view(),
         name='role_registration'),
    path('items', AllRolesPIView.as_view(), name='all_roles'),
    path('items/<str:role_id>', SingleRoleAPIView.as_view(), name='single_role'),
]
