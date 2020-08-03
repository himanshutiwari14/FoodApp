from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import Products
def index(request):
    prod=Products.objects.all()
    if len(prod)==1:
        home_product_display=1

    if len(prod)%4==0:
        home_product_display=len(prod)//2

    home_product_display=(len(prod)//2)+1

    print("here all the products are",prod)
    print(home_product_display,"these number of the products are available rioght now")
    return render(request,'myawsmCart/index.html')

def about_us(request):
    return render(request,'myawsmCart/index2.html')

