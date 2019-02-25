from django.shortcuts import render
from .forms import ItemTypeModelForm
from .models import ItemType
# Create your views here.

def add_item_type(request):
    context={}
    context['ItemType']= ItemType.objects.all()
    context['ItemTypeModelForm'] = ItemTypeModelForm()
    if(request.method=="POST"):
        itemtype_form = ItemTypeModelForm(request.POST)
        if(itemtype_form.is_valid()):
            itemtype_form.save()
            return render(request,"finance/item_type.html",context)
        else:
            return render(request,"finance/item_type.html",context)
    else:
        return render(request,"finance/item_type.html",context)

