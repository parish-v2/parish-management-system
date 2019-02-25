"""parishsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from scheduling import views as scheduling_views

urlpatterns = [
	path('', scheduling_views.index, name='scheduling-index'),
	path('schedule_list/', scheduling_views.ScheduleListView.as_view(), name='scheduling_list'),
	path('schedule_detail/<int:pk>/', scheduling_views.ScheduleDetailView.as_view(), name='scheduling_detail'),
	path('schedule_create/', scheduling_views.ScheduleCreateView.as_view(), name='scheduling_create'),
	path('schedule_update/<int:pk>/', scheduling_views.ScheduleUpdateView.as_view(), name='scheduling_update'),
	path('calendar/', scheduling_views.calendar, name='scheduling_calendar'),
]