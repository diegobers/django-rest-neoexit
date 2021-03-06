from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView

import neoexit_auth.views
from neoexit_auth.forms import NeoExitRegistrationForm
from oferta.views import index, InvestimentoView, OfertaList, OfertaCreate, OfertaDetail, OfertaUpdate, OfertaDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', neoexit_auth.views.perfil, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('accounts/register/', RegistrationView.as_view(form_class=NeoExitRegistrationForm), name='register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    
    path('ofertas/', OfertaList.as_view(), name='oferta'),  
    path('registrar/', OfertaCreate.as_view(), name='registrar'),
    path('oferta/<slug>/', OfertaDetail.as_view(), name='detalhes'),    
    path('alterar/<slug>/', OfertaUpdate.as_view(), name='alterar'),
    path('deletar/<slug>/', OfertaDelete.as_view(), name='deletar'),
    
    path('investir/<slug>/', InvestimentoView.as_view(), name='oferta-detalhe'),  

    #path('investimentos/', InvestimentoListView.as_view(), name='list-investimento'),  
    

    
]