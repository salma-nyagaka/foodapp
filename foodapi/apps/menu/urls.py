from django.urls import path
from .views import MenuAPIView, AllMenuItemsPIView, SingleMenuAPIView


urlpatterns = [
    path('', MenuAPIView.as_view(), name='menu'),
    path('items', AllMenuItemsPIView.as_view(), name='all_menu'),
    path('items/<str:menu_id>', SingleMenuAPIView.as_view(), name='single_menu_item'),

]
