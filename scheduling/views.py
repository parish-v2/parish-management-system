from django.shortcuts import render
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
	# fields = ['title', 'details', 'start_date_time', 'end_date_time']
	form_class = ScheduleForm
	
	# def get_form(self):
	# 	form = super(ScheduleCreateView, self).get_form()
	# 	form.fields['start_date_time'].widget.attrs.update({'class': 'date'})
	# 	form.fields['end_date_time'].widget.attrs.update({'class': 'date'})
	# 	return form

class ScheduleUpdateView(UpdateView):
	model = Schedule
	template_name = "scheduling/schedule_update_form.html"
	fields = ['title', 'details', 'start_date_time', 'end_date_time']

