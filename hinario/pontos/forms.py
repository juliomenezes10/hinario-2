from django.forms import ModelForm
from .models import CreateHinario, Ponto

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class HinarioForm(ModelForm):
    class Meta:
        model = Ponto
        fields = "__all__"
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'mb-3'
        self.helper.form_method = 'post'
        self.helper.form_action = 'pontos:addpontos'

        self.helper.add_input(Submit('submit', 'Submit'))
