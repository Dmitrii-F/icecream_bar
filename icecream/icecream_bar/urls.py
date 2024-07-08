from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'icecream_bar'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('ice_creams/', views.IceCreamsListView.as_view(), name='ice_creams'),
    path('containers/', views.ContainersListView.as_view(), name='containers'),
    path('toppings/', views.ToppingsListView.as_view(), name='toppings'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('all_orders/', views.AllOrdersListView.as_view(), name='all_orders'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('registration/', views.create_account, name='create_account'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('contacts/', views.contacts, name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)