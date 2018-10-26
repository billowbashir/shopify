from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Shop,Product,Order
from .forms import NewShopForm,NewProductForm,NewOrderForm
# from cart.cart import Cart
# from myproducts.models import Product



def home(request):
    shops=Shop.objects.all()
    return render (request,'index.html',{'shops':shops})
    
@login_required(login_url='/accounts/login/')
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
    order_form = NewOrderForm()
    products=Product.objects.filter(shop=shop_id)
    shop=get_object_or_404(Shop,pk=shop_id)
    return render(request,'shop_products.html',{'order_form':order_form,'products':products,'shop':shop})

def add_product(request,pk):

    shop = get_object_or_404(Shop,pk=pk)
    if request.method == 'POST':
        product_form = NewProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.shop=shop
            product.save()
        return redirect('products', shop_id=shop.id)

    else:
        product_form = NewProductForm()

    return render(request, 'new_product.html', {'shop':shop,'order_form':order_form})

def new_order(request,product_id):
    current_user=request.user
    product=get_object_or_404(Product,pk=product_id)

    if request.method == 'POST':
        order_form = NewOrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user=current_user
            order.product=product
            order.save()
        return redirect('/')

    else:
        order_form = NewOrderForm()
    return render(request, 'shop_products.html', {'order_form':order_form,'product':product})

def view_cart(request):
    current_user=request.user
    order=Order.objects.filter(user=current_user)

    return render(request,'cart.html',{'order':order,})
# def add_to_cart(request, product_id, quantity):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.add(product, product.unit_price, quantity)
#
# def remove_from_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.remove(product)
#
# def get_cart(request):
#     return render_to_response('cart.html', dict(cart=Cart(request)))
