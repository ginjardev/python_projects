from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Contact


# Create your views here.
def saveinfo(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact_number = request.POST['phone']

        contact = Contact(first_name= first_name, last_name=last_name, email=email, contact_number=contact_number)
        contact.save()
    
    data = Contact.objects.all()
    return render(request, "index.html", {'Data':data})


def index(request):
    data = Contact.objects.all()
    return render(request, 'index.html', {'Data':data})


def formupdate(request,id):
    if request.method == "POST":
        contact = Contact.objects.get(id=id)
        contact.first_name = request.POST['first_name']
        contact.last_name = request.POST['last_name']
        contact.email = request.POST['email']
        contact.contact_number = request.POST['phone']
        contact.save()
    
    return redirect("index")


def edit(request, id):
    data = Contact.objects.get(id=id)
    data.delete()
    return redirect('index')

def delete(request,id):
    contact = Contact.objects.all()
    contact.delete()
    return redirect('index')

def search(request):
    query = request.GET["query1"]
    data = Contact.objects.filter(contact_number__icontains = query)
    params = {"Data": data}
    return render(request, 'search.html', params)