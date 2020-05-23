from website.models import Enquiry
from django import forms
class EnquiryForms(forms.ModelForm):
    class Meta:
        models = Enquiry    
        fields = "__all__"
