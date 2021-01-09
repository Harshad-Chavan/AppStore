from django import forms
from .models import FileDetails

# class EncryptionForm(forms.Form):
#     orignal_file_name = forms.CharField(label='Orignal file name',max_length=50)
#     action = forms.ChoiceField(label = 'Action', choices=[('Encyrpt','Encyrpt'),('Decyrpt','Decyrpt')])
    
class EncryptionForm(forms.ModelForm):
    class Meta:
        model = FileDetails
        fields = ["file_name","selected_action",]
        
