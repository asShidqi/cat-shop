from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_app' : 'Cat Shop',
        'name': 'Muhammad Fayyed As Shidqi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
