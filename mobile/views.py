from django.shortcuts import render, redirect
from django.db.models import F
from .models import Mobile, Brand
from .forms import MobileForm,BrandForm

# Create your views here.


def main_page(request):
    mobiles = Mobile.objects.all()
    brands = Brand.objects.all()

    context = {
        "mobiles": mobiles,
        "brands": brands,
    }
    return render(request, 'main.html', context)

def show_mobiles(request):
    mobiles = Mobile.objects.all()
    extra_data = None
    if "edited" in request.GET:
        extra_data = "Edit successfuly."
    context = {
        "mobiles": mobiles,
        "extra_data": extra_data,
    }
    return render(request, 'show_mobiles.html', context)

def show_brands(request):
    brands = Brand.objects.all()
    extra_data = None
    if "edited" in request.GET:
        extra_data = "Edit successfuly."
    context = {
        "brands": brands,
        "extra_data": extra_data,
    }
    return render(request, 'show_brands.html', context)

def forms_page(request):
    
    return render(request, 'forms.html')

def add_brand(request):
    submitted = False
    if request.method == 'POST':
        form = BrandForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('/brand/add?submitted=True')
        
    else:
        form = BrandForm
        if "submitted" in request.GET:
            submitted = True
    context = {
        "form": form,
        "submitted": submitted,
    }

    return render(request, "add_brand_form.html", context)


def add_mobile(request):
    submitted = False
    if request.method == 'POST':
        form = MobileForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('/mobile/add?submitted=True')
        
    else:
        form = MobileForm
        if "submitted" in request.GET:
            submitted = True
    context = {
        "form": form,
        "submitted": submitted,
    }

    return render(request, "add_mobile_form.html", context)

def edit_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    if request.method == "POST":
        form = MobileForm(request.POST, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("/mobiles/?edited=True")
        else:
            print("is not valid")
    else:
        form = MobileForm(instance=mobile)
    context = {
        "form": form,
    }

    return render(request, "edit_mobile_form.html", context)

def edit_brand(request, id):
    brand = Brand.objects.get(id=id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)

        if form.is_valid():
            form.save()
            return redirect("/brands/?edited=True")
        else:
            print("is not valid")
    else:
        form = BrandForm(instance=brand)
    context = {
        "form": form,
    }

    return render(request, "edit_brand_form.html", context)


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
            brand_name = 'Brand nationality and Builder country are equal'
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
