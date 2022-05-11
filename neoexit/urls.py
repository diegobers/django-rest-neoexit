from oferta.views import index, oferta_detail
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView

import neoexit_auth.views
from neoexit_auth.forms import NeoExitRegistrationForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('oferta/<slug>/', oferta_detail, name='oferta-detalhes'),    
    path('accounts/profile/', neoexit_auth.views.perfil, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegistrationView.as_view(form_class=NeoExitRegistrationForm), name='register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    
]