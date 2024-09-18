from django.shortcuts import render,redirect
from main.forms import CatEntryForm
from main.models import CatEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    cat_entries = CatEntry.objects.all()
    context = {
        'name_app' : 'Cat Shop',
        'name': 'Muhammad Fayyed As Shidqi',
        'class': 'PBP D',
        'cat_entries': cat_entries
    }

    return render(request, "main.html", context)

def create_cat_entry(request):
    form = CatEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form':form}
    return render(request,"create_cat_entry.html",context)

def show_xml(request):
    data = CatEntry.objects.all()

def show_xml(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CatEntry.objects.all()

def show_json(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")