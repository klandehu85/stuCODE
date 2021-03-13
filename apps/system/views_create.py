from django.views.generic import CreateView

from .mixin import LoginRequiredMixin
from .models import Menu


class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    fields = '__all__'
    success_url = '/system/rbac/menu/create'