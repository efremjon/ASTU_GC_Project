

from http.client import CONTINUE
from multiprocessing import context
from multiprocessing.dummy import JoinableQueue
from operator import attrgetter
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from Agent.models import *
from .form import passwordform,NameForm
from django.core.mail import send_mail

# Create your views here.

def Admin_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()

    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product':all_product,
     
    }
    return render(request,'Company/dashboard/admin.html',context)

def staff_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
   
    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product':all_product,
        'staff_finance_manager' :staff_finance_manager,
        'staff_company_store_manager':staff_company_store_manager,
     
    }
    return render(request,'Company/dashboard/staff.html',context)

def store_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
   
    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'all_store' :all_store,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product':all_product,
        'staff_finance_manager' :staff_finance_manager,
        'staff_company_store_manager':staff_company_store_manager,
     
    }
    return render(request,'Company/dashboard/store.html',context)




def region_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
   
    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'all_store' :all_store,
        'all_region' :all_region,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product':all_product,
        'staff_finance_manager' :staff_finance_manager,
        'staff_company_store_manager':staff_company_store_manager,
     
    }
    return render(request,'Company/dashboard/region.html',context)

def product_dashboard(request):
    all_agent = Agent.objects.all()
    S_staff = Company_Store_Manager.objects.all()
    F_staff = Finance_Manager.objects.all()
    total_agent = all_agent.count()
    tottal_staff = S_staff.count() + F_staff.count()
    all_store = Company_Store.objects.all()
    tottal_store = all_store.count()
    all_region = Region.objects.all()
    tottal_region = all_region.count()
    all_product = Product.objects.all()
    tottal_product = all_product.count()
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
   
    context = {
        'all_agent' : all_agent,
        'total_agent' :total_agent,
        'tottal_staff' : tottal_staff,
        'all_store' :all_store,
        'all_region' :all_region,
        'tottal_store' : tottal_store,
        'tottal_region': tottal_region,
        'tottal_product' : tottal_product,
        'all_product':all_product,
        'staff_finance_manager' :staff_finance_manager,
        'staff_company_store_manager':staff_company_store_manager,
     
    }
    return render(request,'Company/dashboard/product.html',context)

  
def add_agent(request):
    form =NameForm()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Full_Name=first_name+" " +last_name
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        facebook=request.POST['facebook']
        telegram=request.POST['telegram']
        instagram=request.POST['instagram']
        about=request.POST['about']
        profile_pic=request.FILES['img']
        city=request.POST['city']
        address=request.POST['address']
        location=request.POST['location']
        TIN_Num=request.POST['TIN_NO']
        agreement=request.FILES['agreement']
        licenc=request.FILES['licenc']
        form =NameForm(request.POST)
       
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username taken')
                return render(request,'Company/agents/add-agent.html',{})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken ')
                return render(request,'Company/agents/add-agent.html',{})
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                group = Group.objects.get(name='Agent')
                user.groups.add(group)
                Agent.objects.create(user=user,phone1=phone1,phone2=phone2,facebook=facebook,telegram=telegram,instagram=instagram, about=about,profile_pic=profile_pic,city=city,address=address,location=location,TIN_NO=TIN_Num,agreement=agreement,License=licenc,Full_Name=Full_Name)
                messages.success(request, 'Sucssesfull Create User.')
                return redirect ('agent-view')
        else:
            messages.info(request, 'PASSWORD NOT MUCH')
            return render(request,'Company/agents/add-agent.html',{})
    return render(request,'Company/agents/add-agent.html',{'form':form})

# ////////////////

# Profile
def show_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin , 
    }
    return render(request,'Company/profile/show_profile.html',context)

def edit_profile(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
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
    return render(request,'Company/profile/edit_profile.html',context)

def change_password(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    
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
    return render(request, 'Company/profile/chage_password.html', context)

def change_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
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
    return render(request,'Company/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users=User.objects.get(id=request.user.id)
    admin=users.admin
    context = {
        'admin':admin ,
        'usermodel':users
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect ('edit_profile')
    
    return render(request,'Company/profile/edit_profile.html',context)
# end profile

# //////////////

# Manage Staff 
def view_staff(request):
    staff_finance_manager = Finance_Manager.objects.all()
    staff_company_store_manager = Company_Store_Manager.objects.all()
    context = {
       'staff_finance_manager' :staff_finance_manager,
       'staff_company_store_manager':staff_company_store_manager,
    }
    return render(request,'Company/staffs/staff-view.html',context)


def staff_profile(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         context = {'staff_detail':staff_detail}
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    return render(request,'Company/staffs/staff-detail.html',context)


def add_staff(request):
    return render(request,'Company/staffs/add-staff.html',{})

def update_staff(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         
         context = {'staff_detail':staff_detail}
         if request.method == 'POST':
            #  staff_detail.staff=request.POST['job']
             staff_detail.salary=request.POST['salary']
             staff_detail.save()
             return redirect('view-staff')
            
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    

    return render(request,'Company/staffs/update_staff.html',context)

def remove_staff(request,pk,staff):
    if staff=='Finance_manager':
         staff_detail = Finance_Manager.objects.get(id=pk)
         context = {'staff_detail':staff_detail}
    elif staff=='Store_Manager':
        staff_detail= Company_Store_Manager.objects.get(id=pk)
        context = {'staff_detail':staff_detail}
    else:
        context = {}
    return render(request,'Company/staffs/remove_staff.html',context)
    

# end Staff



def view_agent_orders(request):
    return HttpResponse('agent orders')

def approve_agent_orders(request):
    return HttpResponse('agent orders approved')

def store(request):
    return HttpResponse('store')


def contact_store_manager(request):
    return HttpResponse('contact store manager')

def agent_report(request):
    return HttpResponse('agent report')

def finance_report(request):
    return HttpResponse('finance report')


def advertisements(request):
    return HttpResponse('addvertisment')

# agent management

def agent_view(request):
    all_agent = Agent.objects.all()
    context = {
        'all_agent':all_agent,
    }
    return render(request,'Company/agents/agent-view.html',context)

def agent_detail(request,pk):
    agent = Agent.objects.get(pk=pk)
   
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/agent-detail.html',context)

def agent_update_contrat(request,pk):
    agent = Agent.objects.get(pk=pk)
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/update_agent.html',context)

def remove_agent(request,pk):
    agent = Agent.objects.get(pk=pk)
    context = {
        'agent':agent,      
    }
    return render(request,'Company/agents/remove_agent.html',context)
# Manage Store 

def view_store(request):
    all_store = Company_Store.objects.all()
    manager=Company_Store_Manager.objects.all()
    context = {
        'all_store' : all_store,
        'manager' :manager
    }
    return render(request,'Company/store/store-view.html',context)

def add_store_company(request):
    if request.method == 'POST':
        Store_Name=request.POST['store_name']
        Address=request.POST['address']
        store=Company_Store.objects.create(Store_Name=Store_Name,Address=Address)
        Product_Amount_in_Store.objects.create(store=store)
        Company_Store_Manager.objects.create(Store=store)
        Product_Amount_in_Store.objects.create(store=store)
   
        messages.info(request, 'Store Successfully added')
        
        return redirect('view-store')
    else:
        return render(request,'Company/store/add-store.html')
    

def sore_ditel_view(request,pk):
    all_product = Product.objects.all()
    store = Company_Store.objects.get(pk=pk)
    amount_store = Product_Amount_in_Store.objects.get(store=store)
    manager=Company_Store_Manager.objects.get(Store=store)
    
    Total = 0
    Dopple = 'Dopple'
    
    table_data = {}
    for product in all_product:
        table_data[product.Product_Name] = getattr(amount_store, product.Product_Name)
        Total += getattr(amount_store, product.Product_Name)

    context = {
        'all_product' : all_product,
        'store': store,
        'amount': amount_store,
        'table_data': table_data,
        'Total' : Total,
        'a': Dopple,
        'manager' :manager,
    }
    return render(request,'Company/store/store-detail.html',context)

# end Manage store

# Manage Region

def view_region(request):
    all_region = Region.objects.all()
    context = {
        'all_region' : all_region,
    }
    return render(request,'Company/region/region-view.html',context)
def add_region(request):
    return render(request,'Company/region/add-region.html')

# end Region



# Manage Product

def view_product(request):
    all_product = Product.objects.all()
    context = {
        'all_product':all_product,
    }
    return render(request,'Company/product/view-products.html',context)

def add_product(request):
    if request.method == 'POST':
        Product_Name=request.POST['product_name']
        img=request.FILES['add_image']
        Price_in_botle=request.POST['single_price']
        Price_in_creates=request.POST['crate_price']
        Product.objects.create(Product_Name=Product_Name,img=img,Price_in_botle=Price_in_botle,Price_in_creates=Price_in_creates)
        messages.info(request, 'New Product Successfully added')
        return redirect('view-product')
    else:
        return render(request,'Company/product/add-new-product.html')

def update_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.Product_Name=request.POST['product_name']
        product.Price_in_botle=request.POST['single_price']
        product.Price_in_creates=request.POST['crate_price']
        product.save()
        messages.info(request, 'Product Successfully Updated')
        return redirect('view-product')
    context = {
        'product':product,
    }
    return render(request,'Company/product/update-product.html',context)
       
   

# End Product
def advertisments_view(request):
    return render(request,'Company/advertisments/advertisments.html')



def product_in_store(request):
    all_Product_Amount_in_Store = Product_Amount_in_Store.objects.all()
    # p_a=Product_Amount_in_Store.objects.get(Store=1,Product_Name=2)
    all_Product = Product.objects.all()
    all_Company_Store = Company_Store.objects.all()
    

    #  Name, id, produc_store, product_Quintitiy
 
#  store manager


#         price.append(product.Price_in_creates)
#         data=zip(prods,price,quantity,sub_total)
#         quantity.append(getattr(order,product.Product_Name))
#         sub_total.append(product.Price_in_creates*getattr(order,product.Product_Name))
#         grand_total+=float(product.Price_in_creates*getattr(order,product.Product_Name))
#         total_quantity+=(getattr(order,product.Product_Name))
#         VAT_Paid = float(grand_total * 0.15)

#     data=zip(prods,price,quantity,sub_total)

#     context={
#         'transaction':transaction,
#         'data':data,
#         'total_quantity':total_quantity,
#         'grand_total' :grand_total,
#         'VAT':VAT_Paid,
     
#     }
#     return render (request,'Company/store_manager/check_slip.html',context)

def store_manager_view(request):
    table_data={}
    Total=0
    arrimg=[]
    arrvalu=[]
    arrkey=[]
    user = User.objects.get(id=request.user.id)
    all_Product = Product.objects.all()
    company_manager=Company_Store_Manager.objects.get(user=user)
    spesific_store_from_manager=company_manager.Store
    store_id = spesific_store_from_manager.id
    spesific_store = Company_Store.objects.get(id=store_id)
    product_amount=Product_Amount_in_Store.objects.get(store=spesific_store)
    refile_product = add_to_store.objects.filter(Store=spesific_store).order_by('-date_created')
    for product in all_Product:
        arrimg.append(product.img)
        table_data[product.Product_Name]=((getattr(product_amount, product.Product_Name)))
        Total += getattr(product_amount, product.Product_Name)
        
        
    for key,valu in table_data.items():
        arrkey.append(key)
        arrvalu.append(valu)
          
    data=zip(arrkey,arrvalu,arrimg)
       
    context = {
            'table_data' : table_data,
            'Total' : Total,
            'data' : data,
            'company_manager':company_manager,
            'spesific_store': spesific_store,
            'refile_product' : refile_product,
    }

    return render(request,'Company/store_manager/view-store.html',context)
def add_produc_to_store_view(request):
    all_Product = Product.objects.all()
    user = User.objects.get(id=request.user.id)
    company_manager=Company_Store_Manager.objects.get(user=user)
    spesific_store_from_manager=company_manager.Store
    store_id = spesific_store_from_manager.id
    spesific_store = Company_Store.objects.get(id=store_id)
    product_amount=Product_Amount_in_Store.objects.get(store=spesific_store)
    
    name =''
    if request.method == 'POST':
        name = request.POST['product']
        old_amount = getattr(product_amount,name)
        new_amount = request.POST['amount']
        update_amount = old_amount + int(new_amount)
        setattr(product_amount, name , update_amount)
        product_amount.save()
        add_to_store.objects.create(Store=spesific_store,product=name,qunitiy=new_amount)
        messages.info(request, 'Store refilled successfully')
        return redirect('store-manager-home')
    
    context = {
        'all_Product' :all_Product,
       
       
    }
    return render(request,'Company/store_manager/add_to_store.html',context)

def aprove_order_view(request):
    user = User.objects.get(id=request.user.id)
    
    company_manager=Company_Store_Manager.objects.get(user=user)
    spesific_store_from_manager=company_manager.Store
    store_id = spesific_store_from_manager.id
    spesific_store = Company_Store.objects.get(id=store_id)
    product_amount=Product_Amount_in_Store.objects.get(store=spesific_store)
    all_tranaction = Agent_Transaction.objects.filter()
    
    context = {
        'all_tranaction':all_tranaction,
      
    }
    return render(request,'Company/store_manager/approved_orders.html',context)
def approv_order(request):
    # the html file 
    return render(request,'Company/store_manager/approved_orders.html',context)

def stor_check_slip_view(request,pk):
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
    return render (request,'Company/store_manager/check_slip.html',context)

def allow_load_view(request,pk):
    all_tranaction = Agent_Transaction.objects.all()
    approve=Agent_Transaction.objects.get(id=pk)
    x=approve.Agent_order_id
    Or_id =x.id
    update_order=Agent_order.objects.get(id=Or_id)
    update_order.status = 'Recived'
    update_order.save()
    context = {
                'all_tranaction':all_tranaction,
              } 

    return render(request,'Company/store_manager/approved_orders.html',context)


def loaded_order(request):
    all_tranaction = Agent_Transaction.objects.all()
    
    context = {
        'all_tranaction':all_tranaction,
      
    }
    return render(request,'Company/store_manager/loaded.html',context)
# END store manager


# Report
def view_report(request):
    return render(request,'Company/report/a.html',{})

# END Report

#  Finance admin

def finance_admin_view(request):
    all_tranaction = Agent_Transaction.objects.all()
    
    context = {
        'all_tranaction':all_tranaction,
      
    }
    return render(request,'Company/finance/home.html',context)
def check_slip_view(request,pk):
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
    return render(request,'Company/finance/new_order-details.html',context)

def approve_view(request,pk):
    all_tranaction = Agent_Transaction.objects.all()

    approve=Agent_Transaction.objects.get(id=pk)
    x=approve.Agent_order_id
    Or_id =x.id
    update_order=Agent_order.objects.get(id=Or_id)
    update_order.status = 'Approved'
    update_order.save()
   
    context = {
        'all_tranaction':all_tranaction,
      
    }

    return render(request,'Company/finance/home.html',context)

def check_store_view(request):
    return render(request,'Company/finance/check-store.html',{})

def aprove_order_history_view(request):
    all_tranaction = Agent_Transaction.objects.all()
    context = {
        'all_tranaction' : all_tranaction,
    }
    return render(request,'Company/finance/approved-orders-history.html',context)

# END Finance admin