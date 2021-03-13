from django.views.generic import ListView

from apps.custom import SimpleInfoCreateView
from .models import Menu
from .mixin import LoginRequiredMixin


class MenuCreateView(SimpleInfoCreateView):
    model = Menu
    fields = '__all__'
    extra_context = dict(menu_all=Menu.objects.all())

class MenuListView(LoginRequiredMixin, ListView):
    model = Menu
    context_object_name = 'menu_all'