from django import forms

from .models import Clima


class ClimaForm(forms.ModelForm):
    class Meta:
        model = Clima
        fields = [
            "ciudad",
            "fecha_y_hora",
            "temperatura",
        ]
        widgets = {
            "ciudad": forms.Select(attrs={"class": "bg-white text-black"}),
            "fecha_y_hora": forms.DateTimeInput(attrs={"type": "datetime-local","class": "bg-white text-black"}),
            "temperatura": forms.NumberInput(attrs={"class": "bg-white text-black"})
        }