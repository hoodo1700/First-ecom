from django.contrib import admin
from django.urls import path
from . import views 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('headphones/',views.headphones,name='headphones'),
  
    path('electronic/',views.electronic,name='electronic'),
    path('ApplePhones/',views.mobiles,name='ApplePhones'),
    path('samsungphone/',views.samsungphone,name='samsungphone'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('poromotion/',views.poromotion,name='poromotion'),
    path('poromotion/<int:poromotion_id>/',views.poromotion,name='poromotion'),
    
    
    
    
    
    
   
    

    
   
    
]
