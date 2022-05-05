from django.contrib import admin
from django.urls import path
import oferta.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', oferta.views.index),
]
