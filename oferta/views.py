from django.shortcuts import render
from django.utils import timezone
from oferta.models import Oferta

def index(request):
    ofer = Oferta.objects.all()
    #ofer = Oferta.objects.filter(published_at__lte=timezone.now()).select_related("author")
    #logger.debug("%d ofertas", len(ofer))
    return render(request, "oferta/index.html", {"oferta": ofer})


def post_detail(request, slug):
    ofer = get_object_or_404(Oferta, slug=slug)
    
    return render(request, "oferta/oferta-detalhe.html", {"oferta": ofer}) #, "comment_form": comment_form})