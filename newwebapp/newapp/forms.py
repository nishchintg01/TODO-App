from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone_no=forms.IntegerField()
    
