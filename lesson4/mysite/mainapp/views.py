from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView
from .models import GoodModel
from .forms import ProductEditForm


class ItemsListView(ListView):
    model = GoodModel
    template_name = "mainapp/goods_list.html"

    def get_queryset(self):
        items = GoodModel.objects.all()
        return items


def good_add(request):
    if request.method == "POST":
        form = ProductEditForm(data=request.POST)
        return save_good_form(request, form, 'mainapp/good_create.html')
    else:
        form = ProductEditForm()
        return save_good_form(request, form, 'mainapp/good_create.html')


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = GoodModel.objects.all()
            data['html_good_list'] = render_to_string('mainapp/goods_list.html', {
                'object_list': goods
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
