from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Schedule
from .forms import ScheduleForm

# Create your views here.
def index(request):
	return render(request, template_name='scheduling/index.html')

class ScheduleDetailView(DetailView):
	model = Schedule
	template_name = "scheduling/schedule_detail.html"

class ScheduleListView(ListView):
	model = Schedule
	template_name = "scheduling/schedule_list.html"

class ScheduleCreateView(CreateView):
	model = Schedule
	template_name = "scheduling/schedule_create_form.html"
	form_class = ScheduleForm
	success_url = reverse_lazy('scheduling_list')

class ScheduleUpdateView(UpdateView):
	model = Schedule
	template_name = "scheduling/schedule_update_form.html"
	fields = ['title', 'details', 'start_date_time', 'end_date_time']

