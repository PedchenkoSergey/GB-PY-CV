from django.urls import path, include
from .views import ItemsListView, good_add


app_name = 'mainapp'

urlpatterns = [
    path('index/', ItemsListView.as_view(), name='goods-list'),
    path('add_good/', good_add, name='add-good'),
]
