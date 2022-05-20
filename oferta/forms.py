from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.add_input(Submit('submit', 'Comentar'))