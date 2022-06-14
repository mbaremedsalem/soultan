from django.urls import path
from shop.views import index,detail,cart,check,contact,about
urlpatterns = [
    path('',index,name = 'home'),
    path('',index,name = 'index'),
    path('<int:myid>',detail ,name = 'detail'),
    path('checkout/',check, name = 'check'),
    path('contact/',contact,name = 'contact'),
    path('about/',about,name = 'about'),
    path('cart/',cart,name = 'cart'),
] 
