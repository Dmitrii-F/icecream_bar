from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser, Group
from django.http import Http404
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from .models import IceCreamInContainer, Flavor, Container, Topping
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, SignUpForm, IceCreamInContainerForm
from django.contrib.auth import login, authenticate, logout
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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            g = Group.objects.get(name='clients')
            g.user_set.add(user)
            login(request, user)
            return render(request, 'registration/account_created.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/create_account.html', {'form': form})


def logout_view(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return redirect('icecream_bar:index')  # на главную страницу сайта


# class ProfileDetailView(DetailView):
#     model = User
#     pk_url_kwarg = 'id'
#     template_name = 'registration/profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = f'Страница пользователя: {self.object.user.username}'
#         return context

class UserProfileView(TemplateView):
    template_name = 'registration/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     except User.DoesNotExist:
    #         raise Http404("Пользователь не найден")
    #     context['user_profile'] = user
    #     context['title'] = f'Профиль пользователя {user}'
    #     return context


def contacts(request):
    return render(request, 'contacts/contacts.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
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


class OrdersListView(ListView):
    model = IceCreamInContainer
    template_name = 'icecream_bar/orders_list.html'
    context_object_name = 'orders_list'


class OrderCreateView(CreateView):
    model = IceCreamInContainer
    form_class = IceCreamInContainerForm
    template_name = 'icecream_bar/order_create.html'
    success_url = reverse_lazy('icecream_bar:orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self):
        context = super(OrderCreateView, self).get_context_data()
        context['toppings_list'] = Topping.objects.all()
        context['ice_creams_list'] = Flavor.objects.all()
        context['containers_list'] = Container.objects.all()
        return context
