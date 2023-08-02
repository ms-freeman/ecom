from django.shortcuts import render
from .models import Product, SearchQuery

# Create your views here.
def index(request):


    products_object=Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products_object = Product.objects.filter(title__icontains =item_name )
       

    return render(request, 'shop/index.html', {'product_object': products_object})


def detail(request,myid):
    products_object = Product.objects.get(id=myid)
    return render(request,'shop/detail.html',{'product_object': products_object})
