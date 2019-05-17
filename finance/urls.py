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

app_name="finance"

urlpatterns = [
    path('Items/Cash', views.add_item_type, name='add-item-type'),
    path('Items/Cash/<int:item_id>', views.edit_item_type, name='edit-item-type'),
    path('payments/sacrament-payment-history', views.get_sacrament_payment_history, name='sacrament-payment-history'),
    path('payments/purchases', views.purchases, name='purchases'),
    path('payments/add-invoice', views.add_invoice, name='add-invoice'),
    path('payments/invoice/items/<int:invoice_id>/add', views.add_invoice_items, name="add-invoice-item"),
    path('payments/invoice/items/<int:invoice_id>', views.invoice_items, name="invoice-items"),

]
