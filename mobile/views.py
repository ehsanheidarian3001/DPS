from django.shortcuts import render, redirect
from django.db.models import F
from .models import Mobile, Brand
from .forms import MobileForm

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
    print("id:", id)
    mobile = Mobile.objects.get(id=id)
    # form = MobileForm()
    if request.method == "POST":
        form = MobileForm(request.POST, instance=mobile)

        if form.is_valid():
            print("is valid")
            form.save()
            return redirect("/")
        else:
            print("is not valid")

        print("======================")
    else:
        form = MobileForm(instance=mobile)
    context = {
        "form": form,
    }

    return render(request, "mobile_form.html", context)


def reports_page(request):
    filter_number = 0
    brand_name = ''
    if request.method == 'GET':
        if 'f1' in request.GET:
            mobiles = Mobile.objects.filter(brand_id__nationality='Korea')
            brand_name = 'Brand nationality is Korea'
            filter_number = 1
        elif 'f2' in request.GET:
            mobiles = Mobile.objects.none()
            brand_name = 'Search in brand name'
            filter_number = 2
        elif 'f3' in request.GET:
            mobiles = Mobile.objects.filter(builder_country=F('brand_id__nationality'))
            brand_name = 'Brand nationality and Builder country is equal'
            filter_number = 3
        else:
            
            mobiles = Mobile.objects.all()
    elif request.method == 'POST':
        brand_name = request.POST['brand_name']
        mobiles = Mobile.objects.filter(brand_id__name=brand_name)
    context = {
        "mobiles": mobiles,
        "filter_number": filter_number,
        "brand_name": brand_name,
    }
    return render(request, 'reports.html', context)
