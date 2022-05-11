from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def perfil(request):
    return render(request, "neoexit_auth/perfil.html")