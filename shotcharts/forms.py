from django.forms import ModelForm
from api.models import Chart

class ChartForm(ModelForm):

    class Meta:
        model = Chart
        fields = ['name', 'img_url', 'chart_type']