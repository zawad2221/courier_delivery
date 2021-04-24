from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, OrderForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
from .models import Merchant, MerchantInvoice, Order

def getCharge(location, weight):
    print("locatoin",location," weight ",weight)
    charge = 0
    location = int(location)
    weight = int(weight)
    if location==0:
        print("locatoin",location," weight ",weight)
        if weight<=2000:
            charge=60
        elif weight<=3000:
            print("locatoin",location," weight ",weight)
            charge=70
        elif weight<=4000:
            charge=80
        else:
            charge=90
    elif location==1:
        if weight<=2000:
            charge=110
        elif weight<=3000:
            charge=130
        elif weight<=4000:
            charge=150
        else:
            charge=170
        charge = charge*1.51
    elif location==2:
        if weight<=2000:
            charge=130
        elif weight<=3000:
            charge=150
        elif weight<=4000:
            charge=170
        else:
            charge=190
        charge = charge*1.51
    return charge

@csrf_exempt
def order(request):
    if request.method=="POST":
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
            print(orderForm.data['merchent'])
            invoice = MerchantInvoice(merchantId=Merchant.objects.get(id= orderForm.data['merchent']))
            invoice.save()
            charge = getCharge(orderForm.data['deliveryLocation'],orderForm.data['weight'])
            print("charge:",charge)
            order = Order(deliveryLocation=orderForm.data['deliveryLocation'],invoiceId=invoice,weight=orderForm.data['weight'],charge=charge)
            order.save()
    orderForm = OrderForm()
    return render(request,"order.html",{'form':orderForm,'order':Order.objects.all()})

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        print("already")
        return redirect(order)
    if request.method=="GET":
        loginForm = LoginForm()
        return render(request, "login.html", {'form':loginForm})
    if request.method=="POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(request, username=loginForm.cleaned_data["userName"],password=loginForm.cleaned_data["password"])
            if user is not None:
                auth_login(request,user)
                return HttpResponse("logedin")
            else :
                return HttpResponse("loginfailed")

