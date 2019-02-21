from .models import Baptism
import django_tables2 as tables


class BaptismTable(tables.Table):

    id = tables.Column(attrs={
        'th': {'style': 'display:none;'},
        'td': {'style': 'display:none;'},
    })
    status = tables.Column(attrs={
        'td': {'class': 'status'},
    })
    
    class Meta:
        template_name = 'django_tables2/bootstrap.html'
        row_attrs = {
            'class': 'selectable-row table-sm us'
        }
        model = Baptism
        exclude = ('target_price','minister','registry_number','page_number','record_number', 'remarks' )  
        sequence = ('id', 'profile', 'status', 'date', 'target_price', 'minister', 'legitimacy')
        attrs = {'class': 'table table-hover selectable-table table-bordered'}
        template_name = 'sacrament/table.html'