from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Schedule
from .forms import ScheduleForm

# Create your views here.
@login_required(login_url='/login/')
def index(request):
	return render(request, template_name='scheduling/index.html')

class ScheduleDetailView(LoginRequiredMixin, DetailView):
	model = Schedule
	template_name = "scheduling/schedule_detail.html"

	login_url = '/login/'

class ScheduleListView(LoginRequiredMixin, ListView):
	model = Schedule
	template_name = "scheduling/schedule_list.html"

	login_url = '/login/'

class ScheduleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Schedule
	template_name = "scheduling/schedule_create_form.html"
	form_class = ScheduleForm
	success_url = reverse_lazy('scheduling_list')
	success_message = "Event was created successfully scheduled!"

	login_url = '/login/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class ScheduleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Schedule
	template_name = "scheduling/schedule_update_form.html"
	form_class = ScheduleForm
	success_url = reverse_lazy('scheduling_list')
	success_message = "Event was created successfully updated!"

	login_url = '/login/'


def calendar(request):
	context = {}
	context['form'] = ScheduleForm()
	return render(request, template_name='scheduling/example01-basic.html', context=context)