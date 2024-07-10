from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser, Group
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from .forms import FeedbackForm, SignUpForm, IceCreamInContainerForm, UserInfoForm, UserPasswordForm, LoginForm
from .models import IceCreamInContainer, Flavor, Container, Topping


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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            g = Group.objects.get(name='clients')
            g.user_set.add(user)
            login(request, user)
            return render(request, 'registration/account_created.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/create_account.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('icecream_bar:profile')


def logout_view(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return redirect('/')  # на главную страницу сайта


class UserSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/update_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info_form'] = UserInfoForm(instance=self.request.user)
        context['user_password_form'] = UserPasswordForm(self.request.user)
        context['title'] = f'Изменение профиля {self.request.user}'
        return context

    def post(self, request, *args, **kwargs):
        if 'user_info_form' in request.POST:
            form = UserInfoForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                # messages.success(request, 'Данные успешно изменены.')
                return redirect('icecream_bar:profile')
            else:
                context = self.get_context_data(**kwargs)
                context['user_info_form'] = form
                return render(request, self.template_name, context)
        elif 'user_password_form' in request.POST:
            form = UserPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                # messages.success(request, 'Пароль успешно изменён.')
                return self.get(request, *args, **kwargs)
            else:
                context = self.get_context_data(**kwargs)
                context['user_password_form'] = form
                return render(request, self.template_name, context)
        else:
            return self.get(request, *args, **kwargs)


class UserProfileView(TemplateView):
    template_name = 'registration/profile.html'


def contacts(request):
    return render(request, 'contacts/contacts.html')


class IndexView(View):
    def get(self, request):
        return render(request, 'icecream_bar/index.html')


class IceCreamsListView(ListView):
    model = Flavor
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


class AllOrdersListView(ListView):
    model = IceCreamInContainer
    template_name = 'icecream_bar/all_orders.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['orders_list'] = IceCreamInContainer.objects.all()
        return context


class OrdersListView(ListView):
    model = IceCreamInContainer
    template_name = 'icecream_bar/orders_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['orders_list'] = IceCreamInContainer.objects.filter(user=self.request.user)
        return context


class OrderCreateView(CreateView):
    model = IceCreamInContainer
    form_class = IceCreamInContainerForm
    template_name = 'icecream_bar/order_create.html'
    success_url = reverse_lazy('icecream_bar:orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self):
        context = super().get_context_data()
        context['toppings_list'] = Topping.objects.all()
        context['ice_creams_list'] = Flavor.objects.all()
        context['containers_list'] = Container.objects.all()
        return context
