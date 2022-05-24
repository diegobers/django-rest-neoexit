from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from oferta.models import Investimento

@login_required
def perfil(request):

    investimento = Investimento.objects.all()

    return render(request, "neoexit_auth/perfil.html", {"investimento": investimento})