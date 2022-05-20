from http.client import CONTINUE
from itertools import product
from multiprocessing import context
from multiprocessing.dummy import JoinableQueue
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from Agent.models import Customer
from Company.models import Product
from .models import Customer_order
from .form import passwordform
from django.core.mail import send_mail


from django.shortcuts import render

# Create your views here.


def Customer_dashboard(request):
    customer_orders=Customer_order.objects.filter(Customer=request.user.customer)
    products=Product.objects.all()
    orders=customer_orders
    total_pending=0
    total_received=0
    total_paid=0
    total_rejected=0
    total_quantity=[]
    # for order in orders:
    #     for product in products:
    #         total_quantity+=getattr(order,product.Product_Name)
        
    
  
    for order in orders:
        total_paid+=order.total_payment
        if order.status == 'Pending':
            total_pending+=1
        elif order.status == 'Out for delivery':
            total_rejected+=1
        elif order.status == 'Delivered':
            total_received+=1
        total_paid
    context={'customer_orders':customer_orders,
    'total_payment':total_paid,'total_pending':total_pending,
    'total_rejected':total_rejected,
    'total_received':total_received,
    'total_quantity':total_quantity
    }
    return render(request,'Customer/home.html',context)
    
# User Profile
def show_profile(request):
    customer=Customer.objects.get(id=request.user.customer.id)
    context={'customer':customer}
    return render(request,'Customer/profile/show_profile.html',context)

def edit_profile(request):
    users=User.objects.get(id=request.user.id)
    context = {
        'users':users ,
        
    }
    if request.method == 'POST':
        users.customer.about=request.POST['about']
        users.customer.phone1=request.POST['phone1']
        users.customer.phone2=request.POST['phone2']
      #  admin.Company=request.POST['company']
        users.customer.address=request.POST['address']
        

        users.customer.facebook=request.POST['facebook']
        users.customer.telegram=request.POST['telegram']
        users.customer.instagrm=request.POST['instagram']
        users.first_name=request.POST['first_name']
        users.last_name=request.POST['last_name']
        users.email=request.POST['email']
        users.customer.save()
        users.save()
        return redirect ('show_profile_customer')
    return render(request,'Customer/profile/edit_profile.html',context)


def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.customer
    
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
    return render(request, 'Customer/profile/chage_password.html', context)

def change_profile_pic(request):
    return render(request,'Customer/profile/edit_profile.html',)

def delete_profile_pic(request):
    return render(request,'Customer/profile/edit_profile.html',)

# end user profile




def make_order(request):
    products=Product.objects.all()
    
    context={
        'all_product':products,
    
    }

    return render(request,'Customer/cust_order.html',context)

def send_delivery(request):

    delivereds=Customer_order.objects.filter(status='Pending',Customer=request.user.customer)
    products=Product.objects.all()
    tests=delivereds
    quantity=[]
    for test in tests:
        total_quantity=0
        for product in products:
            total_quantity+=getattr(test,product.Product_Name)
        quantity.append(total_quantity)

    context={'deliverds':delivereds,'quantity':quantity}
    return render(request,'Customer/send-delivery-status.html',context)

def transaction_history(request):
    
    customer_orders=Customer_order.objects.filter(Customer=request.user.customer)
    context={'customer_orders':customer_orders}
    return render(request,'Customer/transaction_history.html',context)





def order_summer(request):
    
    ag=Customer_order.objects.create(status='Pending')
    all_product = Product.objects.all()

    ary1=[]
    ary2=[]
    a=0
    tl=0
    arr={}
    if request.method == 'POST':
        for product in all_product:
            a=request.POST[product.Product_Name]
            arr[product.Product_Name]=a
            tp=product.Price_in_creates * int(request.POST[product.Product_Name])
            ary1.append(a)
            ary2.append(tp)
            tl=tl+tp
        
        print(arr)
        for key ,value in arr.items():
            setattr(ag,key,value)
        ag.save()
        
        obj = {
            "process": "Cart",
            "successUrl": "http://localhost:8000/Customer/success/",
            "ipnUrl": "http://localhost:8000/Agent/ipn",
            "cancelUrl": "http://localhost:8000/Customer/cancel",
            "merchantId": "SB1560",
            "merchantOrderId": ag.id,
            "expiresAfter": 24,
            "totalItemsDeliveryFee": 19,
            "totalItemsDiscount": 1,
            "totalItemsHandlingFee": 12,
            "totalItemsTax1": 250,
            "totalItemsTax2": 0
        }
        cart = { "cartitems": [{ "itemId":"sku-01", "itemName":"Beer","unitPrice":tl,"quantity":1},]}
        mylist = zip(all_product,ary1,ary2)        
        context = {
            'all_product' : all_product,
           
            'a':a,
            'ary':ary1,
            'mylist':mylist,
            'tl':tl,
            'obj': obj, 
            'cart': cart

        }
        return render(request,'Customer/order_summer.html',context)
    return redirect('make_order')
    
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
    Customer_Orders=Customer_order.objects.get(id=moi)
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
    
    TC = Customer_Transaction.objects.filter(TransactionCode = TransactionCode)  
   
    if TC.exists():  
        redirect('transactions')
    else:
        Agent_Transaction.objects.create(Agent_order_id=Agent_Orders,Total_Amount=total,Paid_status=status,TransactionCode = TransactionCode,MarchentId=MerchantCode)
    return render(request, 'Customer/post-payment.html',context )

# def cancel(request):
#     return render(request, 'Agent/cancel.html')

# def ipn(request):
#     return render(request, 'Agent/ipn.html')
# def manage_customers(request):

#      return render(request,'Agent/manage-customers.html',{})

# def transaction_detail(request,pk):
#     transaction=Agent_Transaction.objects.get(id=pk) 
#     products=Product.objects.all()
#     order=Agent_order.objects.get(id=transaction.Agent_order_id.id)
#     price=[]
#     prods=[]
#     quantity=[]
#     sub_total=[] 
#     grand_total=0
#     total_quantity=0
#     for product in products:
#         price.append(product.Price_in_creates)
#         prods.append(product.Product_Name)
#         quantity.append(getattr(order,product.Product_Name))
#         sub_total.append(product.Price_in_creates*getattr(order,product.Product_Name))
       
#         total_quantity+=(getattr(order,product.Product_Name))
    
    
   
#     data=zip(prods,price,quantity,sub_total)
#     context={
#         'transaction':transaction,
#         'data':data,
        
#         'total_quantity':total_quantity,
     
       
#     }
#     return render(request,'Agent/transaction-details.html',context)
