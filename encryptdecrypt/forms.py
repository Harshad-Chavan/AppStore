from django import forms

class EncryptionForm(forms.Form):
    orignal_file = forms.FileField()
    encyrpt_file_name = forms.CharField(label='Encrypted file name',max_length=50)
