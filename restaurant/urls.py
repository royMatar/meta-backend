from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('tables/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tables/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
