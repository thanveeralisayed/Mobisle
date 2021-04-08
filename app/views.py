from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,Order
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages


# def home(request):
#     return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        android = Product.objects.filter(category='a')
        iphones = Product.objects.filter(category='i')
        qwerty = Product.objects.filter(category='q')
        keypad = Product.objects.filter(category='k')
        return render(request, 'app/home.html',{'android':android,'iphones':iphones,'qwerty':qwerty,'keypad':keypad})

       


def SearchItem(request):
    item_name = request.GET.get('item_name')
    item = Product.objects.filter(title__icontains=item_name)
    itemser = item_name
    return render(request,'app/aphones.html',{'searcheditems':item,'itemser':itemser})    

    




        

# def product_detail(request):
#  return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self,request,pk):
        prod = Product.objects.get(id=pk)

        return render(request, 'app/productdetail.html',{'prod':prod})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

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
          

    return render(request, 'app/aphones.html',{'mobiles':mobiles , 'brands':brands, 'memory':memory, 'internal':internal, 'br':br})



def iphones(request, data=None):

    br = 'iphone'
    internal = Product.objects.values_list('rom', flat=True).filter(category='i').distinct
    if data == None:
        mobiles = Product.objects.filter(category='i')  

    elif data in str(internal):
         mobiles = Product.objects.filter(category='i').filter(rom=data)      


    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'internal':internal,'br':br})



def qphones(request, data=None):
    br = 'qphone'
    brands = Product.objects.values_list('brand', flat=True).filter(category='q').distinct()

    if data == None:
        mobiles = Product.objects.filter(category='q')

    elif data in brands:
        mobiles = Product.objects.filter(category='q').filter(brand=data)    

    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'brands':brands,'br':br})


def kphones(request, data=None):
    br = 'kphone'
    brands = Product.objects.values_list('brand', flat=True).filter(category='k').distinct()

    if data == None:
        mobiles = Product.objects.filter(category='k')

    elif data in brands:
        mobiles = Product.objects.filter(category='k').filter(brand=data)    

    return render(request, 'app/aphones.html',{'mobiles':mobiles ,'brands':brands,'br':br})






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
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})


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

    if data == None:
        addr = Customer.objects.filter(user=request.user)
        return render(request,'app/profile.html',{'address':addr,'active':'btn-primary'})

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
    
        


