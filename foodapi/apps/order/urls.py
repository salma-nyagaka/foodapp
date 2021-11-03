from django.urls import path
from .views import OrderAPIView, UsersOrdersPIView, SingleOrderAPIView, AllOrdersPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='order'),
    path('user', UsersOrdersPIView.as_view(), name='user_orders'),
    path('<str:pk>', SingleOrderAPIView.as_view(), name='update_single_order_item'),
    path('all', AllOrdersPIView.as_view(), name='all_orders'),

]
