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
from . import views

app_name="sacrament"

urlpatterns = [
    path('', views.index, name='side-bar'),

    # applications
    path('application/baptism', views.add_baptism_application, name='add-baptism-application'),
    path('application/confirmation', views.add_confirmation_application, name='add-confirmation-application'),
    path('application/marriage', views.add_marriage_application, name='add-marriage-application'),

    # update data
    path('update/marriage', views.add_marriage_application, name='add-marriage-application'),


    path('records/baptism', views.view_records_baptism, name='view-records-baptism'),
    path('records/confirmation', views.view_records_confirmation, name='view-records-confirmation'),
    path('records/marriage', views.view_records_marriage, name='view-records-marriage'),


    #post request
    #path('post/baptism/<int:id>', views.post_test, name='post-test'),
    path('post/baptism/<int:b_id>', views.post_retrieve_baptism, name='post-retrieve-baptism'),
    path('post/confirmation/<int:c_id>', views.post_retrieve_confirmation, name='post-retrieve-confirmation'),

    # update
    path('post/', views.post_receive_registry, name='post-receive-registry'),
    path('post/requestregistrynumber',views.post_request_registry_number, name='request-registry-number'),
    
]
