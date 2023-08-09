from django.shortcuts import render
from .models import Mobile, Brand

# Create your views here.


def main_page(request):
    mobiles = Mobile.objects.all()
    brands = Brand.objects.all()

    context = {
        "mobiles": mobiles,
        "brands": brands,
    }
    return render(request, 'main.html', context)


def update_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    context = {
        "mobile": mobile,
    }

    return render(request, "update_mobile.html", context)
