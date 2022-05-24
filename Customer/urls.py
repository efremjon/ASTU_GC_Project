from django.urls import path
from .import views
urlpatterns = [
    path('',views.Customer_dashboard,name="Customer_dashbord"),

    path('show_profile/',views.show_profile,name='show_profile_customer'),
    path('edit_profile/',views.edit_profile,name='edit_profile_customer'),
    path('change_password/',views.change_password,name='change_password_customer'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic_customer'),
    path('delete_profile_pic/',views.delete_profile_pic,name='delete_profile_pic_customer'),


    path('success/',views.success,name="success"),
    path('make_order/',views.make_order,name="make_order"),
    path('order_summer/',views.order_summer,name="customer_order_summer"),
    path('send_delivery/',views.send_delivery,name="send_delivery"),
    path('customer_transactions/',views.customer_transactions,name="customer_transactions"),
    path('customer_transactions/<int:pk>',views.customer_recived,name="customer_recived"),
    path('customer_transactions/<int:pk>',views.customer_not_recived,name="customer_not_recived"),
    
    path('customer-transaction-detail/<int:pk>',views.customer_transaction_detail,name="customer-transaction-detail"),

  
]