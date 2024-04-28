
from django.contrib import admin
from django.urls import path, include
from entry.views import loginPage 
admin.site.login=loginPage 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entry.urls')),
    
]
