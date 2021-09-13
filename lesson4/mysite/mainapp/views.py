from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:goods-list'))
    else:
        form = ProductEditForm()
        return render(request, 'mainapp/good_create.html', {'form': form})
