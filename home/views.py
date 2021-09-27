from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import contact 
from .forms import RegisterContact

# Function for add new contacts in DB
def addContact(request):
    if request.method=="POST":
        fm = RegisterContact(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            mb = fm.cleaned_data['mobile_no']
            reg = contact(name=nm, mobile_no=mb)
            reg.save()
            fm = RegisterContact()
    else:        
        fm = RegisterContact()
    
    contactdata = contact.objects.all()
    return render(request, 'contact.html', {'form':fm, 'data':contactdata}) 

# Function for update contacts
def updateContact(request, id):
    if request.method=='POST':
        pi = contact.objects.get(pk=id)
        fm = RegisterContact(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = contact.objects.get(pk=id)
        fm = RegisterContact(instance=pi)
    return render(request, 'update.html', {'form':fm})


# Function for delete contacts
def deleteContact(request, id):
    if request.method=='POST':
        pi = contact.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')