from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Baptism,Confirmation,Marriage,Minister, SacramentModel
from parishsystem.enums import Status
from .forms import ProfileModelForm,BaptismModelForm,ConfirmationModelForm,MarriageModelForm
from django.http import JsonResponse
from django.core import serializers

def index(request):
    return render(request,"sacrament/side_bar.html")

def add_baptism_application(request):
    context= {}
    if(request.method == "POST"):
        profile_form = ProfileModelForm(request.POST,prefix="profile")
        baptism_form = BaptismModelForm(request.POST,prefix="baptism")
        if profile_form.is_valid() and baptism_form.is_valid():
            profile = profile_form.save()
            baptism = baptism_form.save(commit=False)
            baptism.profile = profile
            baptism.status = SacramentModel.PENDING
            baptism.save()
            return redirect("sacrament:add-baptism-application") 
        else:
            context['BaptismModelForm']= baptism_form
            context['ProfileModelForm']= profile_form
            return render(request,"sacrament/application_baptism.html",context) 
    else:
        context['BaptismModelForm']= BaptismModelForm(prefix="baptism")
        context['ProfileModelForm']= ProfileModelForm(prefix="profile")
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
from .tables import BaptismTable, ConfirmationTable
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
    #return HttpResponse("HELLO!")