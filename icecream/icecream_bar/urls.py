from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'icecream_bar'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ice_creams/', views.IceCreamsListView.as_view(), name='ice_creams'),
    path('containers/', views.ContainersListView.as_view(), name='containers'),
    path('toppings/', views.ToppingsListView.as_view(), name='toppings'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('all_orders/', views.AllOrdersListView.as_view(), name='all_orders'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/change_profile/', views.UserSettingsView.as_view(), name='change_profile'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/feedback/', views.feedback_view, name='feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
