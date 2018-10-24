from django.shortcuts import render,redirect,get_object_or_404
from .models import Shop,Product
from .forms import NewShopForm
def home(request):
    shops=Shop.objects.all()
    return render (request,'index.html',{'shops':shops})

def new_shop(request):
    current_user=request.user
    if request.method=='POST':
        shop_form=NewShopForm(request.POST,request.FILES)
        if shop_form.is_valid():
            shop=shop_form.save(commit=False)
            shop.owner=current_user
            shop.save()
        return redirect('Home')
    else:
        shop_form=NewShopForm()
        return render(request,'new_shop.html',{'form':shop_form})

def shop_products(request,shop_id):
    products=Product.objects.filter(shop=shop_id)
    shop=get_object_or_404(Shop,pk=shop_id)
    return render(request,'shop_products.html',{'products':products,'shop':shop})

def add_product(request,pk)
