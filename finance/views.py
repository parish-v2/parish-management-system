from django.shortcuts import render, redirect
from .forms import ItemTypeModelForm
from .models import ItemType
from .models import ItemType, Invoice, InvoiceItem, InvoiceGeneric, InvoiceItemGeneric
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

def edit_item_type(request,item_id):
    context={}
    context['ItemTypeModelForm'] = ItemTypeModelForm(instance=ItemType.objects.get(id=item_id))
    if(request.method=="POST"):
        itemtype_form = ItemTypeModelForm(request.POST, instance=ItemType.objects.get(id=item_id))
        if(itemtype_form.is_valid()):
            itemtype_form.save()
            return redirect("/finance/Items/Cash")
        else:
            return render(request,"finance/item_type_edit.html",context)
    else:
        return render(request,"finance/item_type_edit.html",context)
def get_sacrament_payment_history(request):
    """This returns the list of payments
    for a sacrament.
    """
    profile = None
    if request.GET.get("sacrament")=="baptism":
        profile = Baptism.objects.get(id=int(request.GET.get("id"))).profile
        invoiceItems = InvoiceItem.objects.filter(invoice__profile_A=profile, item_type=ItemType.objects.get(name="Baptism")).order_by('-id')
        totalPaid = sum([i.amount_paid for i in invoiceItems]) + sum([i.discount for i in invoiceItems])
        print(totalPaid)
        response = {"invoices":[], "balance":invoiceItems[0].balance}
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



from django_tables2 import RequestConfig
import django_tables2 as tables
# This is the generic class of a selectable table.
class AbstractTable(tables.Table):
    id = tables.Column(attrs={
        'th': {'style': 'display:none;'},
        'td': {'style': 'display:none;'},
    })
    class Meta:
        
        row_attrs = {
            'class': 'selectable-row table-sm us'
        }
        template_name = 'django_tables2/bootstrap.html'
        template_name = 'sacrament/table.html'
        attrs = {'class': 'table table-hover selectable-table table-bordered records-table'}
    


# Custom tables start here.
class InvoiceTable(AbstractTable):
    status = tables.Column(attrs={
        'td': {'class': 'status'},
    })
    
    class Meta(AbstractTable.Meta):
        model = InvoiceGeneric
        #sequence = ('id', 'profile', 'status', 'date', 'target_price', 'minister', 'legitimacy')


def purchases(request):
    table = InvoiceTable(InvoiceGeneric.objects.all())
    RequestConfig(request,paginate={'per_page': 20}).configure(table)
    context = {
        "table":table,
    }   
    return render(request,"finance/invoices.html",context)

def add_invoice(request):
    context = {}
    return render(request,"finance/add_invoice.html",context)
   
