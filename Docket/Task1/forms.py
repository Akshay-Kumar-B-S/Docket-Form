from django import forms
from .models import Docket

class DocketForm(forms.ModelForm):
    class Meta:
        model = Docket
        fields = ['name', 'start_time', 'end_time', 'hours_worked', 'rate_per_hour', 'supplier_name', 'purchase_order']
