from django import forms

class StockerForm(forms.Form):
    idno = forms.IntegerField()
    name = forms.CharField()
    contact_no = forms.IntegerField()
    password = forms.CharField()

class AddDispatcherForm(forms.Form):
    idno = forms.IntegerField()
    name = forms.CharField()
    contact_no = forms.IntegerField()
    password = forms.CharField()