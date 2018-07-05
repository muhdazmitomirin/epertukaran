from django import forms
from .models import Bahagian
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class BahagianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BahagianForm, self).__init__(*args, **kwargs)
        
        #Add class to all fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit_change', 'Submit', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "tambah_bahagian" %}>Reset</a>'))

    class Meta:
        model = Bahagian
        fields = ('nama', 'createdby',)