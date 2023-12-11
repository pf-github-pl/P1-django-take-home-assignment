from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class LocationForm(forms.Form):

    latitude = forms.CharField()
    longitude = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(
            Submit('submit',
                   'Find food trucks nearby',
                   css_class="btn btn-primary rounded-pill w-100"
                   )
        )
