from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

# Create your views here.
def home(request):
  items = Item.objects.all()
  return render(request, 'index.html', {'items': items })

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'
  success_url = '/'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'