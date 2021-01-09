from django.shortcuts import render,redirect
from .forms import EncryptionForm
from .models import FileDetails,Action
from .encryptor import Encryptor

# Create your views here.
def encdecHome(request):
    if request.method == 'POST':    
        filled_form = EncryptionForm(request.POST,request.FILES)
        if filled_form.is_valid():
            Encryptor_obj = Encryptor()
            
            selected_action = filled_form.cleaned_data['selected_action']
            file_name = filled_form.cleaned_data['file_name']
            
            if selected_action.action == "Encrypt":
                key = Encryptor_obj.generate_Key_file()
                obj = FileDetails(user = request.user,file_name = file_name,key = key,selected_action = selected_action)
                obj.save()
                note = f"Thanks for using this app.File {file_name} is {selected_action.action}ed"
            elif selected_action.action == "Decrypt":
                note = f"Thanks for using this app.File {file_name} is {selected_action.action}ed"
            new_eform = EncryptionForm()
            return render(request,'encdec_home.html',{'new_form':new_eform,'note':note})
    else:
        note = None
        eform = EncryptionForm()
        return render(request,'encdec_home.html',{'eform':eform,'note':note})

