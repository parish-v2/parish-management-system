from django.shortcuts import render,redirect
from django.http import HttpResponse
from sacrament.models import Profile,Baptism,Confirmation,Marriage,Minister, SacramentModel,Sponsor
from parishsystem.enums import Status,Sacrament
from sacrament.forms import ProfileModelForm, BaptismModelForm, ConfirmationModelForm, MarriageModelForm ,SponsorModelForm ,formset_factory,RequiredFormSet
from django.http import JsonResponse
from django.core import serializers
from sacrament.tables import BaptismTable, ConfirmationTable, MarriageTable
from finance.forms import InvoiceModelForm_Application, InvoiceItemModelForm_Application
from finance.models import Invoice, InvoiceItem, ItemType
from datetime import datetime
from scheduling.models import Schedule



def post_retrieve_baptism(request, b_id):
    b = Baptism.objects.get(id=b_id)
    p = b.profile
    m = b.minister

    sponsors = []
    for x in b.sponsors.all():
        sponsors.append({
            "name":f"{x.last_name}, {x.first_name} {x.middle_name}",
            "residence": x.residence
        })

    return JsonResponse({
        "name":f"{p.last_name}, {p.first_name} {p.middle_name}",
        "suffix":p.suffix,
        "birthdate":p.birthdate,
        "gender":p.get_gender_display(),
        "legitimacy":b.get_legitimacy_display(),
        "birthplace":p.birthplace,
        "minister":f"{m.last_name}, {m.first_name} {m.middle_name}",
        "status":b.get_status_display(),
        "sponsors": sponsors,
    })

def post_retrieve_confirmation(request, c_id):
    c = Confirmation.objects.get(id=c_id)
    p = c.profile
    m = c.minister

    sponsors = []
    for x in c.sponsors.all():
        sponsors.append({
            "name":f"{x.last_name}, {x.first_name} {x.middle_name}",
            "residence": x.residence
        })

    return JsonResponse({
        "name":f"{p.last_name}, {p.first_name} {p.middle_name}",
        "suffix":p.suffix,
        "birthdate":p.birthdate,
        "gender":p.get_gender_display(),
        "birthplace":p.birthplace,
        "minister":f"{m.last_name}, {m.first_name} {m.middle_name}",
        "status":c.get_status_display(),
        "sponsors": sponsors,
        "date": c.date,
    })
    #return HttpResponse("HELLO!")

def update_record(request):
    
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        sacrament = request.POST.get('sacrament')

        print(request.POST)
        if sacrament == "baptism":
            b = Baptism.objects.get(id=id)
            
            #b = Baptism.objects.get(id=b_id)

        profile = b.profile
        # personal details
        profile.first_name = request.POST.get('first_name')
        profile.middle_name = request.POST.get('middle_name')
        profile.last_name = request.POST.get('last_name')
        profile.suffix = request.POST.get('suffix')
        profile.gender = request.POST.get('gender')
        profile.birthdate = request.POST.get('birthdate')
        profile.birthplace = request.POST.get('birthplace')
        b.legitimacy = request.POST.get('legitimacy')

        b.mother_first_name = request.POST.get('mother_first_name')
        b.mother_middle_name = request.POST.get('mother_middle_name')
        b.mother_last_name = request.POST.get('mother_last_name')
        b.mother_suffix = request.POST.get('mother_suffix')

        b.father_first_name = request.POST.get('mother_first_name')
        b.father_middle_name = request.POST.get('mother_middle_name')
        b.father_last_name = request.POST.get('mother_last_name')
        b.father_suffix = request.POST.get('mother_suffix')

        b.minister = Minister.objects.get(id=int(request.POST.get('minister')))

        # Registry details.
        b.registry_number = request.POST.get('registry_number')
        b.record_number = request.POST.get('record_number')
        b.page_number = request.POST.get('page_number')
        b.status = request.POST.get('status')
        b.save()
        profile.save()

        
        if b.status == SacramentModel.APPROVED:
            title="Success!"
            msg="Baptism is approved."
            msgtype="success"
        else:
            title="Info updated"
            msg="Baptism updated but not yet approved."
            msgtype="info"
        return JsonResponse({
            "msgtype": msgtype,
            "title": title,
            "msg":msg 
        })
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def post_request_registry_number(request):
    print(request.POST.get('sacrament'))
    print(request.POST.get('id'))
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        sacrament = request.POST.get('sacrament')
        if sacrament == "baptism":
            b = Baptism.objects.get(id=id)
        profile = b.profile
        minister = b.minister
        return JsonResponse({
            # profile details
            "first_name": profile.first_name,
            "middle_name":profile.middle_name,
            "last_name":profile.last_name,
            "suffix": profile.suffix,
            "status":b.status,
            "gender": profile.gender,
            "birthdate": profile.birthdate,
            "birthplace": profile.birthplace,
            "legitimacy": b.legitimacy,
            "minister": b.minister.id,
            "minister_name": f"{str(b.minister)}",
            "mother_first_name": b.mother_first_name,
            "mother_middle_name": b.mother_middle_name,
            "mother_last_name": b.mother_last_name,
            "mother_suffix": b.mother_suffix,
            "father_first_name": b.father_first_name,
            "father_middle_name": b.father_middle_name,
            "father_last_name": b.father_last_name,
            "father_suffix": b.father_suffix,
            "registry_number":b.registry_number if b.registry_number else "",
            "record_number":b.record_number if b.record_number else "",
            "page_number":b.page_number if b.page_number else "",
        })
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def get_payment_details(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        sacrament = request.POST.get('sacrament')
        if sacrament == "baptism":
            b = Baptism.objects.get(id=id)
        profile = b.profile
        minister = b.minister
        return JsonResponse({
            # profile details
            "first_name": profile.first_name,
            "middle_name":profile.middle_name,
            "last_name":profile.last_name,
            "suffix": profile.suffix,
            "status":b.status,
            "gender": profile.gender,
            "birthdate": profile.birthdate,
            "birthplace": profile.birthplace,
            "legitimacy": b.legitimacy,
            "minister": b.minister.id,
            "minister_name": f"{str(b.minister)}",
            "mother_first_name": b.mother_first_name,
            "mother_middle_name": b.mother_middle_name,
            "mother_last_name": b.mother_last_name,
            "mother_suffix": b.mother_suffix,
            "father_first_name": b.father_first_name,
            "father_middle_name": b.father_middle_name,
            "father_last_name": b.father_last_name,
            "father_suffix": b.father_suffix,
            "registry_number":b.registry_number if b.registry_number else "",
            "record_number":b.record_number if b.record_number else "",
            "page_number":b.page_number if b.page_number else "",
        })
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

from datetime import datetime
def add_sacrament_payment(request):
    """
    STEPS:
    1. Add Invoice
    2. Add Invoice Item
    3. When displaying, return only the laman of the invoice (expected 1 invoice item.)
    """
    if request.method=='POST':
        sacrament=None
        if request.POST.get("sacrament") == "baptism":
            sacrament = Baptism.objects.get(id=int(request.POST.get("id")))
            invoicea = Invoice(
                date_issued=request.POST.get("date"),
                or_number = request.POST.get("or_number"),
                received_by = request.POST.get("received_by"),
                profile_A = sacrament.profile
            )
            invoicea.save()
            ii = InvoiceItem(
                invoice=invoicea,
                item_type=ItemType.objects.get(name="Baptism"),
                quantity=1,
                balance = float(InvoiceItem.objects.filter(invoice__profile_A=sacrament.profile, item_type=ItemType.objects.get(name="Baptism")).order_by('-id')[0].balance)-float(request.POST.get("amount_paid"))-float(request.POST.get("discount")),
                amount_paid = request.POST.get("amount_paid"),
                discount = request.POST.get("discount"),
            )
            if ii.balance<0:
                raise Exception("Amount paid exceeds balance.")
            ii.save()
    return HttpResponse("done");

def get_payment_history(request):
    return JsonResponse();

    

"""
class Invoice(models.Model):
    date_issued = models.DateField()
    or_number = models.IntegerField()
    received_by = models.CharField(max_length=255) # name that appears on the actual invoice
    profile_A = models.ForeignKey(
        Profile, 
        on_delete=models.PROTECT,
        related_name='profile_A',
        null=True, 
        blank=True
    )
    profile_B = models.ForeignKey(
        Profile, 
        on_delete=models.PROTECT,
        related_name='profile_B',
        null=True, 
        blank=True
    )
"""



