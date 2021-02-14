from django.forms import ModelForm
from .models import BadHabbit, Subs

class BadHabbitForm(ModelForm):
    
    class Meta:
        model = BadHabbit
        fields = ['title', 'description', 'dangers']

class SubsForm(ModelForm):
    
    class Meta:
        model = Subs
        fields = ['title', 'description','bad_id', 'badget_min', 'badget_max', 'efficacite', 'duration']
