from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='order'),
    # path('orders', AllOrderItemsPIView.as_view(), name='all_orders'),
    # path('orders/<str:order_id>', SingleOrderAPIView.as_view(), name='single_order_item'),

]
