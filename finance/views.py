from django.shortcuts import render
from .forms import ItemTypeModelForm
from .models import ItemType
# Create your views here.

def add_item_type(request):
    context={}
    if(request.method=="POST"):
        pass
    else:
        context['ItemTypeModelForm'] = ItemTypeModelForm()
        context['ItemType']= ItemType.objects.all()
        return render(request,"finance/item_type.html",context)
