from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Baptism,Confirmation,Marriage,Minister, SacramentModel,Sponsor
from parishsystem.enums import Status,Sacrament
from .forms import ProfileModelForm, BaptismModelForm, ConfirmationModelForm, MarriageModelForm ,SponsorModelForm ,formset_factory
from django.http import JsonResponse
from django.core import serializers
from .tables import BaptismTable, ConfirmationTable, MarriageTable
from finance.forms import InvoiceModelForm_Application, InvoiceItemModelForm_Application
from finance.models import Invoice, InvoiceItem, ItemType
from datetime import datetime
def index(request):
    return render(request,"sacrament/side_bar.html")

def add_baptism_application(request):
    context= {}
    SponsorFormset = formset_factory(SponsorModelForm ,extra=2, can_delete=True)
    if(request.method == "POST"):
        profile_form = ProfileModelForm(request.POST,prefix="profile")
        baptism_form = BaptismModelForm(request.POST,prefix="baptism")
        sponsor_formset = SponsorFormset(request.POST) 
        invoice_form = InvoiceModelForm_Application(request.POST,prefix="invoice")
        invoice_item_form = InvoiceItemModelForm_Application(request.POST,prefix="invoice_item")
        if profile_form.is_valid() and baptism_form.is_valid() and invoice_form.is_valid() and invoice_item_form.is_valid():
            profile = profile_form.save()
            baptism = baptism_form.save(commit=False)
            baptism.profile = profile
            baptism.status = SacramentModel.PENDING
            baptism.save()
            for form in sponsor_formset:
                if(form.is_valid()):
                    f = form.save()
                    f.baptism = baptism
                    f.save()




#if one form is empty and saved then it gets saved as NONE
#sponsors not referenced to baptism
#if cloned it copies text
#cloned does not save

            # if(sponsor_formset.is_valid()):
            #     for form in sponsor_formset:
            #         print("-------ITS TRUE")
            #         print(form)
            #         f = form.save()
            #         f.baptism = baptism
            #         f.save()
            invoice = invoice_form.save(commit=False)
            invoice.profiles = [profile]
            invoice.date_issued = datetime.now().date()
            invoice.save()
            item = invoice_item_form.save(commit=False)
            item.invoice= invoice
            item.item_type = ItemType.objects.get(name="Baptism")
            item.quantity = 1
            item.save()
            return redirect("sacrament:add-baptism-application") 
        else:
            context['SponsorFormset']= sponsor_formset
            context['BaptismModelForm']= baptism_form
            context['ProfileModelForm']= profile_form
            context['InvoiceModelForm_Application']= invoice_form
            context['InvoiceItemModelForm_Application']= invoice_item_formset()
            return render(request,"sacrament/application_baptism.html",context) 
    else:
        suggested_price = ItemType.objects.get(name="Baptism").suggested_price
        context['SponsorFormset']= SponsorFormset()
        context['BaptismModelForm']= BaptismModelForm(prefix="baptism")
        context['ProfileModelForm']= ProfileModelForm(prefix="profile")
        context['InvoiceModelForm_Application']= InvoiceModelForm_Application(prefix="invoice")
        context['InvoiceItemModelForm_Application']= InvoiceItemModelForm_Application(prefix="invoice_item", initial={'balance':suggested_price})
        return render(request,"sacrament/application_baptism.html",context) 
    

def add_confirmation_application(request):
    context= {}
    if(request.method == "POST"):
        profile_form = ProfileModelForm(request.POST,prefix="profile")
        confirmation_form = ConfirmationModelForm(request.POST,prefix="confirmation")
        if profile_form.is_valid() and confirmation_form.is_valid():
            profile = profile_form.save()
            confirmation = confirmation_form.save(commit=False)
            confirmation.profile = profile
            confirmation.status = SacramentModel.PENDING
            confirmation.save()
            return redirect("sacrament:add-confirmation-application") 
        else:
            context['ConfirmationModelForm']= confirmation_form
            context['ProfileModelForm']= profile_form
            return render(request,"sacrament/application_confirmation.html",context) 
    else:
        context['ConfirmationModelForm']= ConfirmationModelForm(prefix="confirmation")
        context['ProfileModelForm']= ProfileModelForm(prefix="profile")
        return render(request,"sacrament/application_confirmation.html",context)

def add_marriage_application(request):
    context={}
    if(request.method=="POST"):
        groom_form = ProfileModelForm(request.POST,prefix="groom")
        bride_form = ProfileModelForm(request.POST,prefix="bride")
        marriage_form = MarriageModelForm(request.POST,prefix="marriage")
        if groom_form.is_valid() and bride_form.is_valid() and marriage_form.is_valid():
            groom = groom_form.save()
            bride = bride_form.save()
            marriage = marriage_form.save(commit=False)
            marriage.groom_profile = groom
            marriage.bride_profile = bride
            marriage.status = SacramentModel.PENDING
            marriage.save()
            return redirect("sacrament:add-marriage-application") 
    else:
        context['MarriageModelForm']= ConfirmationModelForm(prefix="marriage")
        context['GroomModelForm']= ProfileModelForm(initial={'gender':Profile.MALE},prefix="groom")
        context['BrideModelForm']= ProfileModelForm(initial={'gender':Profile.FEMALE},prefix="bride")
        return render(request,"sacrament/application_marriage.html",context)
































"""
    MANUAL WAY= KEEP FOR REFERENCE
    if request.method == 'POST':
        profile = Profile.objects.get_or_create(
            first_name = request.POST['first_name'],
            middle_name = request.POST['middle_name'],
            last_name = request.POST['last_name'],
            suffix = request.POST['suffix'],
            birthdate = request.POST['birthdate'],
            gender = request.POST['gender'],
            birthplace = request.POST['birthplace'],
            residence = request.POST['residence']
        )  

        baptism = Baptism.objects.create(
            minister = request.POST['minister'],
            profile = profile,
            legitimacy = request.POST['legitimacy']
        )
        return HttpResponse("hello")
    else:
        ministers = Minister.objects.exclude(status = Status.INACTIVE)
        legitimacy = Baptism.
        context['ministers'] = ministers
        return render(request,"sacrament/application_baptism.html",context)
    """
from django_tables2 import RequestConfig
def view_records_baptism(request):
    table = BaptismTable(Baptism.objects.all())
    RequestConfig(request,paginate={'per_page': 20}).configure(table)
    context = {
        "table":table,
    }   
    return render(request, "sacrament/records_baptism.html", context)

def view_records_confirmation(request):
    table = ConfirmationTable(Confirmation.objects.all())
    RequestConfig(request,paginate={'per_page': 20}).configure(table)
    context = {
        "table":table,
    }   
    return render(request, "sacrament/records_confirmation.html", context)

def view_records_marriage(request):
    table = MarriageTable(Marriage.objects.all())
    RequestConfig(request,paginate={'per_page': 20}).configure(table)
    context = {
        "table":table,
    }   
    return render(request, "sacrament/records_marriage.html", context)

def view_baptism_detail(request, bap_id):
    pass


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
            
        b.registry_number = registry_number
        b.record_number = record_number
        b.page_number = page_number
        b.save()

        return HttpResponse(
            "YO!"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )