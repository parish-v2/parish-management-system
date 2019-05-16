from django.shortcuts import render
from .forms import ItemTypeModelForm
from .models import ItemType
from .models import ItemType, Invoice, InvoiceItem
from django.http import JsonResponse
from sacrament.models import Baptism, Confirmation, Marriage
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

def get_sacrament_payment_history(request):
    """This returns the list of payments
    for a sacrament.
    """
    profile = None
    if request.GET.get("sacrament")=="baptism":
        profile = Baptism.objects.get(id=int(request.GET.get("id"))).profile
        invoiceItems = InvoiceItem.objects.filter(invoice__profile_A=profile, item_type=ItemType.objects.get(name="Baptism"))
        totalPaid = sum([i.amount_paid for i in invoiceItems]) + sum([i.discount for i in invoiceItems])
        print(totalPaid)
        response = {"invoices":[], "balance":totalPaid}
        for ii in invoiceItems:
            response["invoices"].append(
                {
                    "date_issued":ii.invoice.date_issued,
                    "received_by":ii.invoice.received_by,
                    "amount_paid":ii.amount_paid,
                    "discount":ii.discount,
                    "or_no":ii.invoice.or_number,
                    "total":ii.discount+ii.amount_paid, # total
                }
            )
    return JsonResponse(response)