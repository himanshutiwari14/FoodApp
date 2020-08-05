from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import Products
import math
def index(request):
    products_aval=Products.objects.all()
    if len(products_aval)==1:
        slides_required=1
    if len(products_aval)%3==0:
        slides_required=len(products_aval)//3
    else:
        slides_required=(len(products_aval)//3)+1
    params={"number_of_produsts":len(products_aval),"actual_prodcuts":products_aval,"range":range(1,slides_required)}
    return render(request,'myawsmCart/index.html',params)

def about_us(request):
    return render(request,'myawsmCart/index2.html')

