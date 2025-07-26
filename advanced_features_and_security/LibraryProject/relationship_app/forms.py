from django import forms

class ExampleForm(forms.Form):
    field1 = forms.CharField(max_length=100)
    field2 = forms.IntegerField()