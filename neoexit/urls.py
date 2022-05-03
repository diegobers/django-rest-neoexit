from django.contrib import admin
from django.urls import path
import neoexit_auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', neoexit_auth.views.index),
]
