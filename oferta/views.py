from django.shortcuts import render
from django.utils import timezone
from oferta.models import Oferta

def index(request):
    ofer = Oferta.objects.filter(published_at__lte=timezone.now()).select_related("author")
    #logger.debug("%d ofertas", len(ofer))
    return render(request, "blog/index.html", {"oferta": ofer})