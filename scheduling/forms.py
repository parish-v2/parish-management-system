from django import forms
from tempus_dominus.widgets import DateTimePicker
from .models import Schedule
from datetime import datetime, timedelta

class ScheduleForm(forms.ModelForm):
	start_date_time = forms.DateTimeField(
		initial=datetime.now,  # set initial value to now
		widget=DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': False,
					'sideBySide': True,
					'format': 'MMM D, YYYY h:mm A'
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': True,
					'icon_toggle': True,
					'class': 'form-input',
				}),
		input_formats=[
						'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
						'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
						'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
						'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
						'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
						'%m/%d/%y %H:%M',       # '10/25/06 14:30'
						'%b %d, %Y %I:%M %p']		# 'October 25, 2006 2:30 AM' Custom format
	)

	end_date_time = forms.DateTimeField(
		initial=datetime.now() + timedelta(hours=1),  # set initial value to now + 1 hour
		widget=DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': False,
					'sideBySide': True,
					'format': 'MMM D, YYYY h:mm A'
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': True,
					'icon_toggle': True,
					'class': 'form-input',
				}),
		input_formats=[
						'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
						'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
						'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
						'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
						'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
						'%m/%d/%y %H:%M',       # '10/25/06 14:30'
						'%b %d, %Y %I:%M %p']		# 'October 25, 2006 2:30 AM' Custom format
	)

	class Meta:
		model = Schedule
		# fields = '__all__'  # use all fields
		fields = ['title', 'details', 'start_date_time', 'end_date_time']