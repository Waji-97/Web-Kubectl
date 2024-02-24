from .models import Session
from django import forms

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['cluster_name', 'shell', 'prometheus', 'alertmanager', 'grafana']