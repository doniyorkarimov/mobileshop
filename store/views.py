from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import *
from django.db.models import Q


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse('habar junatildi!!!')
    context = {'form': form}
    return render(request, 'contact.html', context)

def product(request, pk):
    productobj = Product.objects.get(id=pk)
    context = {'product': productobj}
    return render(request, 'product.html', context)

def search(request):
    if request.method == 'POST':
        key = str(request.POST['search'])
        products = Product.objects.filter(Q(name__contains=key) | Q(category__name__contains=key))
    return render(request,'search.html',{'products':set(products)})
