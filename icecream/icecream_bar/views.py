from django.views import View
from django.views.generic import ListView, CreateView
from .models import IceCreamInContainer, Container, Topping, Order, Profile
from django.shortcuts import render, redirect
from .forms import FeedbackForm, OrderForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'icecream_bar/feedback.html', {'form': form})

def create_account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(user=user,
            #                        phone_number=form.cleaned_data.get('phone_number'),
            #                        address=form.cleaned_data.get('address'))
            Profile.user = user
            Profile.address = form.cleaned_data.get('address')
            Profile.phone_number = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'registration/account_created.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/create_account.html', {'form': form})

def contacts(request):
    return render(request, 'contacts/contacts.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'icecream_bar/index.html')

class IceCreamsListView(ListView):
    model = IceCreamInContainer
    template_name = 'icecream_bar/ice_creams_list.html'
    context_object_name = 'ice_creams_list'

class ContainersListView(ListView):
    model = Container
    template_name = 'icecream_bar/containers_list.html'
    context_object_name = 'containers_list'

class ToppingsListView(ListView):
    model = Topping
    template_name = 'icecream_bar/toppings_list.html'
    context_object_name = 'toppings_list'

class OrdersListView(ListView):
    model = Order
    template_name = 'icecream_bar/orders_list.html'
    context_object_name = 'orders_list'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'icecream_bar/order_create.html'
    success_url = reverse_lazy('icecream_bar:index')