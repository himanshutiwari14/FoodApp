from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import Products
import math
def index(request):
    prod=Products.objects.all()
    print(len(prod))
    if len(prod)==0:
        slides_required=1

    if len(prod)%4==0:
        slides_required=len(prod)//4

    slides_required=len(prod)// 4 + math.ceil((len(prod) / 4) - (len(prod) // 4))
    print(slides_required,"sr")
    all_prods=[[prod,range(1,len(prod),slides_required)],[prod,range(1,len(prod),slides_required)]]

    params = {'all_prods':all_prods}
   
    return render(request,'myawsmCart/index3.html',params)

def about_us(request):
    return render(request,'myawsmCart/index2.html')

