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

def post_receive_registry(request):
    
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        registry_number = request.POST.get('registry_number')
        record_number = request.POST.get('record_number')
        page_number = request.POST.get('page_number')
        sacrament = request.POST.get('sacrament')

        if sacrament == "baptism":
            b = Baptism.objects.get(id=id)
            #b = Baptism.objects.get(id=b_id)

        #p = b.profile
        #m = b.minister

        b.registry_number = registry_number
        b.record_number = record_number
        b.page_number = page_number
        b.status = SacramentModel.APPROVED
        b.save()

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


            "registry_number":b.registry_number if b.registry_number else "",
            "record_number":b.record_number if b.record_number else "",
            "page_number":b.page_number if b.page_number else "",
        })
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

