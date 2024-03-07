from django.contrib import admin
from django.urls import path
from customers.views import index,index2,index3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index ),
    path('index2/',index2 ),
    path('index3/',index3 ),
]