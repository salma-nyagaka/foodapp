from django.urls import path
from .views import OrderAPIView, UsersOrdersPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='order'),
    path('user', UsersOrdersPIView.as_view(), name='user_orders'),
    # path('orders/<str:order_id>', SingleOrderAPIView.as_view(), name='single_order_item'),

]
