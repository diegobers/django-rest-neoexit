from oferta.views import index, oferta_detail
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('oferta/<slug>/', oferta_detail, name='oferta-detalhes'),
    #path("accounts/profile/", oferta_auth.views.profile, name="profile"),
]