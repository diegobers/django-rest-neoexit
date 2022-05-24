from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from .models import Comentario, Investimento


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.add_input(Submit('submit', 'Comentar'))

class InvestimentoForm(forms.ModelForm):
    class Meta:
        model = Investimento
        fields = ["value", "cota_qtd"]

    def __init__(self, *args, **kwargs):
        super(InvestimentoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.add_input(Submit('submit', 'Investir'))