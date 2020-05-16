from django import forms
from secondapp.models import Users

class FormsgetModel(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
    def clean(self):
        all_clean_data = super().clean()
        print('inside clean')
