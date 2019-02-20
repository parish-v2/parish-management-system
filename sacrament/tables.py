from .models import Baptism
import django_tables2 as tables


class BaptismTable(tables.Table):

    id = tables.Column(attrs={
        'th': {'style': 'display:none;'},
        'td': {'style': 'display:none;'},
        })

    class Meta:
        template_name = 'django_tables2/bootstrap.html'
        row_attrs = {
            'class': 'selectable-row'
            
        }
        model = Baptism
        
        sequence = ('id', 'profile', 'status', 'date', 'target_price', 'minister', 'legitimacy')
        attrs = {'class': 'table table-hover selectable-table table-bordered'}
        template_name = 'sacrament/table.html'