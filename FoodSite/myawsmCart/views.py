from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import Products
import math
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    print("views.py aa rha hai")
    catprods = Products.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    print("what is inside cats",cats)
    for cat in cats:
        print("1")
        print(cat,"cat is")
        prod = Products.objects.filter(category=cat)
        print(prod,"prod is")
        print("2")
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        print("3")
        allProds.append([prod, range(1, nSlides), nSlides])
    print("what is indise all pros",allProds)
    params = {'allProds':allProds}
    return render(request, 'myawsmCart/index.html', params)


