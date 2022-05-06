from django.contrib import admin
from django.urls import path
import oferta.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', oferta.views.index, name='index'),
    path('oferta/<slug>/', oferta.views.oferta_detail, name='oferta-detalhes'),
    #path("accounts/profile/", oferta_auth.views.profile, name="profile"),
]