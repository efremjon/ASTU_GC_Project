from django.urls import path
from .import views
urlpatterns = [
   
    path('',views.Agent_dashboard,name="agent_dashbord"),
    path('my_draiver',views.my_draiver,name="my_draiver"),
    path('my_vichile',views.my_vichile,name="my_vichile"),
    path('my_product',views.my_product,name="my_product"),



#   profile part

    path('show_profile/',views.show_profile,name='show_profile_agent'),
    path('edit_profile/',views.edit_profile,name='edit_profile_agent'),
    path('change_password/',views.change_password,name='change_password_agent'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic_agent'),
    path('delete_profile_pic/',views.delete_profile_pic,name='delete_profile_pic_agent'),



    path('cusomer_order/',views.customer_order,name="customer_order"),
    path('cusomer_order_ditel/<int:pk>',views.cusomer_order_ditel,name="cusomer_order_ditel"),



    path('success/', views.success, name='success'),
    path('agent_make_order/',views.make_order,name="agent_make_order"),
    path('order_summer/',views.order_summer,name="order_summer"),
 
     path('transaction_detail/<int:pk>',views.transaction_detail,name="transaction-detail"),
   
    path('cancel/', views.cancel, name='cancel'),
    path('ipn/', views.ipn, name='ipn'),


    path('add_customers/',views.add_customers,name="add-customers"),
    path('cust_change_password/<int:pk>',views.cust_change_password,name="cust_change_password"),
    path('manage_customers/',views.manage_customers,name="manage_customers"),
    path('customers_ditel/<int:pk>/',views.customers_ditel,name="customers-ditel"),
    path('customers_delete/<int:pk>/',views.customers_delete,name="customers-delete"),
    path('product_in_store/',views.product_in_store,name="product-in-store"),
    path('manage_vehicles/', views.manage_vehicles, name="manage_vehicles"),
    path('add_vehicle/', views.add_vehicle, name="add_vehicle"),
    path('add_driver/', views.add_driver, name="add_driver"),
    path('manage_drivers/',views.manage_drivers,name="manage_drivers"),
    path('transactions/',views.transactions,name="transactions"),
    path('send_message/',views.send_message,name="send_message"),

]
