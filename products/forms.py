from django import forms

class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=3)
    description = forms.CharField()
    rate = forms.FloatField()

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=3)