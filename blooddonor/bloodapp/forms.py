from django import forms

class DonorSearchForm(forms.Form):
    blood = forms.CharField(max_length=10, required=True, label='Blood')
    address = forms.CharField(max_length=255, required=True, label='address')
