from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,Order
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse


# def home(request):
#     return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        num = None
        android = Product.objects.filter(category='a')
        iphones = Product.objects.filter(category='i')
        qwerty = Product.objects.filter(category='q')
        keypad = Product.objects.filter(category='k')
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            num = cart.count()
        return render(request, 'app/home.html',{'android':android,'iphones':iphones,'qwerty':qwerty,'keypad':keypad,'num':num})

       


def SearchItem(request):
    num = None
    item_name = request.GET.get('item_name')
    item = Product.objects.filter(title__icontains=item_name)
    itemser = item_name
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=user)
        num = cart.count()
    return render(request,'app/aphones.html',{'searcheditems':item,'itemser':itemser,'num':num})    

    




        

# def product_detail(request):
#  return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self,request,pk):
        num = None
        present = ''
        user = request.user
        prod = Product.objects.get(id=pk)
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()
            present = ''
            for item in cart:
                print(item.product.id)
                if prod.id == item.product.id:
                    present = 'Yes'
                    print(present)
                    if present == 'Yes':
                        break
                else:
                    present = ''
                    print(present)

        


        return render(request, 'app/productdetail.html',{'prod':prod,'present':present,'num':num})



def add_to_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        user = request.user
        proditem = Product.objects.get(id=prod_id)
        Cart(user=user,product=proditem).save()
        cart = Cart.objects.all().filter(user=request.user).count()





        data = {
            'count':cart
        }

    return JsonResponse(data)


def addedorno(request):
    btnstatus = 'n'
    lsstorage = 'enabled'
    btnclass = 'btn btn-primary shadow px-5 py-2 mt-2'
    btnname = 'Add to Cart'
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            prod = Product.objects.get(id=prod_id)
            present = ''
            for item in cart:
                print(item.product.id)
                if prod.id == item.product.id:
                    present = 'Yes'
                    print(present)
                    if present == 'Yes':
                        btnclass = 'btn btn-secondary shadow px-5 py-2 mt-2'
                        btnname = 'Added to Cart'
                        btnstatus = 'y'
                        lsstorage = 'disabled'
                        print("w")
                        break

        print("works")
       
        data = {
            'classname':btnclass,
            'btnname':btnname,
            'btnstatus':btnstatus,
            'lsstatus':lsstorage
        }   
    return JsonResponse(data)                
        





def removefromcart(request):
    if request.method == "GET":
        itemid = request.GET.get('prod_id')
        print(itemid)
        item = Cart.objects.get(id=itemid)
        Cart.delete(item)
        user = request.user
        cart = Cart.objects.filter(user=user)
        num = cart.count()

        amount = 0.0
        shipping_amt = 70.0


        for item in cart:
            amount = amount + (item.product.d_price * item.quantity)

        total = amount + shipping_amt

        data = {           
            'amount':amount,
            'totalamount':total,
            'count':num
        }

    return JsonResponse(data)        



    
    

    



def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        cart = Cart.objects.filter(user=request.user)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()

        amount = 0.0
        shipping_amt = 70.0


        for item in cart:
            amount = amount + (item.product.d_price * item.quantity)

        total = amount + shipping_amt

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':total
        }

    return JsonResponse(data)  


def cartupdate(request):
    if request.method == "GET":
        cart = Cart.objects.all().filter(user=request.user).count()
        print(cart)

        data = {
            'count':cart
        }
    return JsonResponse(data)        

          







def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        cart = Cart.objects.filter(user=request.user)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()

        amount = 0.0
        shipping_amt = 70.0


        for item in cart:
            amount = amount + (item.product.d_price * item.quantity)

        total = amount + shipping_amt

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':total
        }

    return JsonResponse(data)  
      




def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        num = cart.count()

        amount = 0.0
        shipping_amt = 70.0

        for item in cart:
            amount = amount + (item.product.d_price * item.quantity)

        total = amount + shipping_amt


        return render(request, 'app/addtocart.html',{'carts':cart,'num':num,'amount':amount,'total':total})


def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

# def address(request):
#  return render(request, 'app/profile.html',{'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')



def aphones(request, data=None):

    user = request.user
    num = None
    if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

    br = 'android'
    brands = Product.objects.values_list('brand', flat=True).filter(category='a').distinct()
    memory = Product.objects.values_list('ram', flat=True).filter(category='a').distinct
    internal = Product.objects.values_list('rom', flat=True).filter(category='a').distinct

    if data == None:
        mobiles = Product.objects.filter(category='a')        

    elif data in brands:
        mobiles = Product.objects.filter(category='a').filter(brand=data)

    elif data in str(memory):
         mobiles = Product.objects.filter(category='a').filter(ram=data)  

    elif data in str(internal):
         mobiles = Product.objects.filter(category='a').filter(rom=data)  

    elif data in 'Below':
        mobiles = Product.objects.filter(category='a').filter(d_price__lt=9999)

    elif data in 'Above':
        mobiles = Product.objects.filter(category='a').filter(d_price__gt=9999)    
          

    return render(request, 'app/aphones.html',{'mobiles':mobiles , 'brands':brands, 'memory':memory, 'internal':internal, 'br':br,'num':num})



def iphones(request, data=None):

    user = request.user
    num = None
    if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

    br = 'iphone'
    internal = Product.objects.values_list('rom', flat=True).filter(category='i').distinct
    if data == None:
        mobiles = Product.objects.filter(category='i')  

    elif data in str(internal):
         mobiles = Product.objects.filter(category='i').filter(rom=data)      


    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'internal':internal,'br':br,'num':num})



def qphones(request, data=None):
    user = request.user
    num = None
    if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

    br = 'qphone'
    brands = Product.objects.values_list('brand', flat=True).filter(category='q').distinct()

    if data == None:
        mobiles = Product.objects.filter(category='q')

    elif data in brands:
        mobiles = Product.objects.filter(category='q').filter(brand=data)    

    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'brands':brands,'br':br,'num':num})


def kphones(request, data=None):
    user = request.user
    num = None
    if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

    br = 'kphone'
    brands = Product.objects.values_list('brand', flat=True).filter(category='k').distinct()

    if data == None:
        mobiles = Product.objects.filter(category='k')

    elif data in brands:
        mobiles = Product.objects.filter(category='k').filter(brand=data)    

    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'brands':brands,'br':br,'num':num})






# def login(request):
#     registration = 'no'
#     return render(request, 'app/reglogin.html',{'reg':registration})

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


class CustomerRegistrationView(View):

    
    def get(self, request):
        registration = 'yes'
        form = CustomerRegistrationForm
        return render(request, 'app/reglogin.html',{'form':form,'reg': registration})
        
    def post(self, request):
        registration = 'yes'
        form = CustomerRegistrationForm(request.POST)  
        if form.is_valid(): 
            messages.success(request, 'Registration succesfull') 
            form.save()
        return render(request, 'app/reglogin.html',{'form':form,'reg':registration})



def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self, request):
        user = request.user
        num = None
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary','num':num})


    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            landmark = form.cleaned_data['landmark']
            place = form.cleaned_data['place']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=usr,name=name,landmark=landmark,place=place,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request, 'Address added')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})    

def AddressView(request,data=None):

    user = request.user
    num = None
    if request.user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            num = cart.count()

    if data == None:
        addr = Customer.objects.filter(user=request.user)
        return render(request,'app/profile.html',{'address':addr,'active':'btn-primary','num':num})

    else:
        data = int(data)
        deladd = Customer.objects.get(id=data)
        Customer.delete(deladd)
        return redirect('address')


def SetAddressDefault(request,data):
    data = int(data)
    Customer.objects.filter(user=request.user).update(adefault='No')
    Customer.objects.filter(id=data).update(adefault='Yes')
    
     
    return redirect('address')        
    
        


