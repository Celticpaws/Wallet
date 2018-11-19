from django import forms

from .models import *

class OutcomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OutcomeForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset =  Category.objects.all()

    class Meta:
        model = Outcome
        fields = ('date', 'amount', 'description', 'category','account')
        
class IncomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Income
        fields = ('date', 'amount', 'description', 'payed','account')
        