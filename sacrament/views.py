from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Baptism,Minister, SacramentModel
from parishsystem.enums import Status
from .forms import ProfileModelForm,BaptismModelForm
def index(request):
    return render(request,"sacrament/side_bar.html")
def add_baptism_application(request):
    context= {}
    if(request.method == "POST"):
        profile_form = ProfileModelForm(request.POST,prefix="profile")
        baptism_form = BaptismModelForm(request.POST,prefix="baptism")
        print(request.POST)
        if profile_form.is_valid() or baptism_form.is_valid():
            profile = profile_form.save()
            baptism = baptism_form.save()
            baptism.profile = profile.id
            baptism.save()
        else:
            context['BaptismModelForm']= baptism_form
            context['ProfileModelForm']= profile_form
            return render(request,"sacrament/application_baptism.html",context) 
    else:
        context['BaptismModelForm']= BaptismModelForm(prefix="baptism")
        context['ProfileModelForm']= ProfileModelForm(prefix="profile")
        return render(request,"sacrament/application_baptism.html",context) 
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
from .tables import BaptismTable
from django_tables2 import RequestConfig
def view_records_baptism(request):
    table = BaptismTable(Baptism.objects.all())
    RequestConfig(request,paginate={'per_page': 25}).configure(table)

    context = {
        "table":table,
    }
    return render(request, "sacrament/records_baptism.html", context)

def view_baptism_detail(request, bap_id):
    pass
