from django.urls import path 
from api.views import order_views as views

urlpatterns = [
    path('add/', views.addOrderItems, name='orders-add'),
    path('my-orders/', views.getMyOrders, name='my-orders'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
