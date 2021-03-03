from django.shortcuts import render, redirect
from .models import Products, HomeMakeOver, BeautyProduct, SanityWare, Stationary
from django.contrib import messages

# Create your views here.
def index(request):
    homeMake  = HomeMakeOver.objects.all()
    beautyProduct=BeautyProduct.objects.all()
    sanity=SanityWare.objects.all()
    station=Stationary.objects.all()
    return render(request, 'html/index.html', {'homeMake':homeMake,'beautyProduct':beautyProduct,'sanity':sanity,'station':station})

def Details_Image(request):
    product = Products.objects.all()
    print(product)
    return render(request, 'html/index.html', {'params':product})

def Product(request):
    if request.method=="POST":
        Product_name=request.POST.get('product_name')
        Category=request.POST.get('category')
        SubCategory=request.POST.get('sub_category')
        Price=request.POST.get('price')
        ProductDesc=request.POST.get('product_desc')
        PubDate=request.POST.get('pub_date')
        ProductImage=request.POST.get('product_image')
        addP=Products(product_name=Product_name, Category=Category, Sub_Category=SubCategory, price=Price, product_Desc=ProductDesc, pub_date=PubDate, product_image=ProductImage)
        addP.save()
        messages.success(request, "Your prodcut has been saved!!!")
        return redirect('Addproduct')
    return render(request, 'html/addProduct.html')


def showHome(request):
    allHome = HomeMakeOver.objects.all()
    return render(request,'html/prodcts.html',{'allproducts':allHome})

def showBeauty(request):
    allBeauty = BeautyProduct.objects.all()
    return render(request,'html/prodcts.html',{'allproducts':allBeauty})

def showSanitry(request):
    allSanitry = SanityWare.objects.all()
    return render(request,'html/prodcts.html',{'allproducts':allSanitry})

def showStationary(request):
    allStationary = Stationary.objects.all()
    return render(request,'html/prodcts.html',{'allproducts':allStationary})
