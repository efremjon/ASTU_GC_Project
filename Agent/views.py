from multiprocessing import context
from operator import attrgetter
from statistics import quantiles
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from .form import *
from .models import *
from Company.models import * 
# from Customer.models import Customer_order,Customer_Transaction
import requests
from passlib.hash import pbkdf2_sha256
import json



# Create your views here.
# Dashbord part
def Agent_dashboard(request):
    context={}
    try:
        users=User.objects.get(id=request.user.id)
       
    except users.DoesNotExist:
            return HttpResponse('404,User: Data Not Found')


    try:
        request_agent =Agent.objects.get(user=users)
        all_customer=Customer.objects.filter(Agent=request_agent)
        total_customer = all_customer.count()
        context = {
        'all_customer':all_customer,
        'total_customer':total_customer,
          }
        return render(request,'Agent/agent-dashboard.html',context)
    except request_agent.DoesNotExist:
            return HttpResponse('404,User: Data Not Found')
    
   
    
    


def my_draiver(request):

    return render(request,'Agent/my_draiver.html',{})
def my_vichile(request):

    return render(request,'Agent/my_vichile.html',{})
def my_product(request):

    return render(request,'Agent/my_product.html',{})


# user profile part

def show_profile(request):
    return render(request,'Agent/profile/show_profile.html')

def edit_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    context = {
        'admin':admin ,
        
    }
    if request.method == 'POST':
        admin.about=request.POST['about']
        admin.phone1=request.POST['phone']
        admin.Company=request.POST['company']
        admin.Country=request.POST['country']
        admin.Job=request.POST['job']
        admin.address=request.POST['address']
        admin.facebook=request.POST['facebook']
        admin.telegram=request.POST['telegram']
        admin.instagram=request.POST['instagram']
        users.first_name=request.POST['first_name']
        users.last_name=request.POST['last_name']
        users.email=request.POST['email']
        admin.save()
        users.save()
        return redirect ('show_profile')
    return render(request,'Agent/profile/edit_profile.html',context)


def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    
    if request.method == 'POST':
        form = passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('show_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordform(request.user)
    context = {
        'admin':admin ,
        'usermodel':users,
        'form':form
    }
    return render(request, 'Agent/profile/chage_password.html', context)
def change_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if request.method == 'POST':
        if len(request.FILES['img']) != 0:
            admin.profile_pic.delete()
            admin.profile_pic=request.FILES['img']
            admin.save()
            return redirect ('edit_profile')
        else:
            return render(request,'Company/profile/change_profile_pic.html',context)
    return render(request,'Agent/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.agent
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect ('edit_profile')
    
    return render(request,'Agent/profile/edit_profile.html',context)

# end user profile part





def customer_order(request):
    cust_order={}
    customer_order=[]
    agent_custome=[]
    cust_tran=[]

    users = User.objects.get(id=request.user.id)
    request_agent = Agent.objects.get(user=users)
    agent_customer = Customer.objects.filter(Agent=request_agent)

    for agent_cust in agent_customer:
        cust_order[agent_cust]=Customer_order.objects.filter(Customer=agent_cust)

    for customer, order in cust_order.items():
        customer_order.append(order)
        agent_custome.append(customer)

    for key ,value in cust_order.items():
        for val in value:
            print(val)

    all=Customer_Transaction.objects.all()
    for key in all:
        print(key.Customer_order_id)
         

    data=zip(customer_order,agent_custome)
  
    context = {
         
         'cust_order':cust_order,
         'data':data,
         'customer_order':customer_order
     }
    print(cust_order)
    return render(request,'Agent/view-cust-orders.html',context)
     
def cusomer_order_ditel(request,pk):
    transaction=Customer_Transaction.objects.get(id=pk) 
    products=Product.objects.all()
    order=Customer_order.objects.get(id=transaction.Customer_order_id.id)
    price=[]
    prods=[]
    quantity=[]
    sub_total=[] 
    grand_total=0
    total_quantity=0
    for product in products:
        price.append(product.Price_in_creates)
        prods.append(product.Product_Name)
        quantity.append(getattr(order,product.Product_Name))
        sub_total.append(product.Price_in_creates*getattr(order,product.Product_Name))
       
        total_quantity+=(getattr(order,product.Product_Name))
    data=zip(prods,price,quantity,sub_total)
    context={
        'transaction':transaction,
        'data':data,
        'total_quantity':total_quantity,
        }
    return render(request,'Agent/customer_order_ditel.html',context)

def make_order(request):
     all_product = Product.objects.all()
     all_store = Company_Store.objects.all()
     context = {
         'all_product' : all_product,
         'all_store':all_store,
        
     }
     return render(request,'Agent/agent_order.html',context)

def order_summer(request):
    #  b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    
    all_product = Product.objects.all()
    all_store = Company_Store.objects.all()
    ary1=[]
    ary2=[]
    q=0
    a=0
    tl=0
    arr={}
    arr3=[]
    if request.method == 'POST':
        store = request.POST['store']
        storee=Company_Store.objects.get(Store_Name=store)
        ag=Agent_order.objects.create(status='Pending',Store=storee)
        for product in all_product:
            a=request.POST[product.Product_Name]
            arr[product.Product_Name]=a
            tp=product.Price_in_creates * int(request.POST[product.Product_Name])
            ary1.append(a)
            ary2.append(tp)
            tl=tl+tp
            q+=int(a)
            vat=0.15 * tl
        for key ,value in arr.items():
            setattr(ag,key,value)
        ag.save()
        
        obj = {
            "process": "Cart",
            "successUrl": "http://localhost:8000/Agent/success/",
            "ipnUrl": "http://localhost:8000/Agent/ipn",
            "cancelUrl": "http://localhost:8000/Agent/cancel",
            "merchantId": "SB1560",
            "merchantOrderId": ag.id,
            "expiresAfter": 24,
            "totalItemsDeliveryFee": 0,
            "totalItemsDiscount": 0,
            "totalItemsHandlingFee": 0,
            "totalItemsTax1": vat,
            "totalItemsTax2": 0
        }
        cart = { "cartitems": [{ "itemId":"sku-01", "itemName":"Beer","unitPrice":tl,"quantity":1},]}
        mylist = zip(all_product,ary1,ary2)        
        context = {
            'all_product' : all_product,
            'all_store':all_store,
            'a':a,
            'ary':ary1,
            'mylist':mylist,
            'tl':tl,
            'obj': obj, 
            'cart': cart,
            'q':q
            

        }
        return render(request,'Agent/order_summer.html',context)
    return redirect('agent_make_order')
    
def success(request):

    ii= request.GET.get('itemId')
    total = request.GET.get('TotalAmount')
    moi = request.GET.get('MerchantOrderId')
    ti = request.GET.get('TransactionId')
    status = request.GET.get('Status')
    TransactionCode = request.GET.get('TransactionCode')
    MerchantCode = request.GET.get('MerchantCode')
    BuyerId = request.GET.get('BuyerId')
    Currency = request.GET.get('Currency')

    url = 'https://testapi.yenepay.com/api/verify/pdt/'
    datax = {
        "requestType": "PDT",
        "pdtToken": "Q1woj27RY1EBsm",
        "transactionId": ti,
        "merchantOrderId": moi
    }
    x = requests.post(url, datax)
    if x.status_code == 200:
        print("It's Paid")
    else:
        print('Invalid payment process')
    Agent_Orders=Agent_order.objects.get(id=moi)
    context = {
        'total': total, 
        'status': status,
        'TransactionCode' :TransactionCode,
        'MerchantCode' : MerchantCode,
        'BuyerId' : BuyerId,
        'Currency' :Currency,
        'moi':moi,
        'Agent_Orders':Agent_Orders,

        }
    
    TC = Agent_Transaction.objects.filter(TransactionCode = TransactionCode)  
   
    if TC.exists():  
        redirect('transactions')
    else:
        Agent_Transaction.objects.create(Agent_order_id=Agent_Orders,Total_Amount=total,Paid_status=status,TransactionCode = TransactionCode,MarchentId=MerchantCode)
    return render(request, 'Agent/new_post-payment.html',context )

def cancel(request):
    return render(request, 'Agent/cancel.html')

def ipn(request):
    return render(request, 'Agent/ipn.html')
def manage_customers(request):
    users=User.objects.get(id=request.user.id)
    request_agent =Agent.objects.get(user=users)
    all_customer=Customer.objects.filter(Agent=request_agent)
    total_customer = all_customer.count()
   
    context = {
        'all_customer':all_customer,
        'total_customer':total_customer,
    }
    return render(request,'Agent/manage-customers.html',context)


def add_customers(request):
    
    return render(request,'Agent/add-customer.html')


def customers_ditel(request,pk):
    customer=Customer.objects.get(id=pk)
    context={
        'customer':customer,
    }
    return render(request,'Agent/customer-ditel.html',context)

def customers_delete(request,pk):
    pass
#     customer=Customer.objects.get(id=pk)
#     customer.delete()
#     customer.save()
#     print(customer)
#     return render(request,'Agent/manage-customers.html',)



def product_in_store(request):
    return render(request,'Agent/product-in-agent-store.html',{})




def transaction_detail(request,pk):
    transaction=Agent_Transaction.objects.get(id=pk) 
    products=Product.objects.all()
    order=Agent_order.objects.get(id=transaction.Agent_order_id.id)
    price=[]
    prods=[]
    quantity=[]
    sub_total=[] 
    grand_total=0
    VAT_Paid=0.0
    total_quantity=0
    for product in products:
        price.append(product.Price_in_creates)
        prods.append(product.Product_Name)
        quantity.append(getattr(order,product.Product_Name))
        sub_total.append(product.Price_in_creates*getattr(order,product.Product_Name))
        grand_total+=float(product.Price_in_creates*getattr(order,product.Product_Name))
        total_quantity+=(getattr(order,product.Product_Name))
        VAT_Paid = float(grand_total * 0.15)

    data=zip(prods,price,quantity,sub_total)

    context={
        'transaction':transaction,
        'data':data,
        'total_quantity':total_quantity,
        'grand_total' :grand_total,
        'VAT':VAT_Paid,
     
    }
    return render(request,'Agent/transaction-details.html',context)

def add_vehicle(request):
    return render(request, 'Agent/add-vehicle.html', {})

def manage_vehicles(request):
    return render(request, 'Agent/manage-vehicles.html', {})

def add_driver(request):
    return render(request, 'Agent/add-driver.html', {})

def manage_drivers(request):
     return render(request,'Agent/manage-drivers.html',{})

def transactions(request):

    all_transaction = Agent_Transaction.objects.all().order_by('-date_created')
    context = {
    'all_transaction' :all_transaction,
    }
    return render(request,'Agent/transactions.html',context)


def send_message(request):

     return render(request,'Agent/send-message.html',{})


def cust_change_password(request,pk):
    if request.method=='POST':
        old_password=request.POST.get('password')
        customer=Customer.objects.get(id=pk)
        if customer.user.check_password(old_password):
            new_password=request.POST.get('newpassword')
            renew_password=request.POST.get('renewpassword')
            if new_password == renew_password:
                customer.user.set_password(new_password)
                customer.user.save()
                return HttpResponse('password changed ,successfully')
            return HttpResponse('old password and new password are not the same')
        return HttpResponse('old password doestn\'t exixt in the system')
    return render(request,'Agent/manage-customers.html')
            



        
      
    