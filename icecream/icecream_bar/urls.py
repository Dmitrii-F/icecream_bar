from django.urls import path, include
from icecream_bar import views
app_name = 'icecream_bar'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('ice_creams/', views.IceCreamsListView.as_view(), name='ice_creams'),
    path('cups/', views.CupsListView.as_view(), name='cups'),
    path('toppings/', views.ToppingsListView.as_view(), name='toppings'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('accounts/', include('django.contrib.auth.urls')),
]