from django.shortcuts import render,redirect
from main.forms import CatEntryForm
from main.models import CatEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    cat_entries = CatEntry.objects.filter(user=request.user)
    
    context = {
        'name_app' : 'Cat Shop',
        'name': 'Muhammad Fayyed As Shidqi',
        'class': 'PBP D',
        'user_login': request.user.username,
        'cat_entries': cat_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_cat_entry(request):
    form = CatEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        cat_entry = form.save(commit=False)
        cat_entry.user = request.user
        cat_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_cat_entry.html", context)

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

#fungsi untuk login
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_cat(request, id):
    # Get mood entry berdasarkan id
    cat = CatEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = CatEntryForm(request.POST or None, instance=cat)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_cat.html", context)

def delete_cat(request, id):
    # Get mood berdasarkan id
    cat = CatEntry.objects.get(pk = id)
    # Hapus mood
    cat.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))