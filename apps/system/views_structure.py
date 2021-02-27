from django.views.generic.base import TemplateView

from .mixin import LoginRequiredMixin


class StructureView(LoginRequiredMixin, TemplateView):

    template_name = 'system/structure/structure.html'

import json

from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Structure
from .forms import StructureForm
from django.shortcuts import get_object_or_404

class StructureCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict(structure_all=Structure.objects.all())
        # 判断如果request.GET中包含id,则返回该条数据信息
        if 'id' in request.GET and request.GET['id']:
            structure = get_object_or_404(Structure, pk=request.GET['id'])
            ret['structure'] = structure
        return render(request, 'system/structure/structure_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        # 如果 request.POST中包含id则查找该实例，并传递给ModelForm关键字参数instance，通过调用save()方法，将修改信息保存到该实例。
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST['id'])
        # 如果request.POST中ID值不存在，则使用空的模型作为instance关键参数，调用save()方法，保存新建的数据。
        else:
            structure = Structure()
        structure_form = StructureForm(request.POST, instance=structure)
        if structure_form.is_valid():
            structure_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')

class StructureListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'type', 'parent__name']
        ret = dict(data=list(Structure.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')