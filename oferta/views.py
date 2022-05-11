from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from oferta.models import Oferta
from oferta.forms import ComentarioForm


def index(request):
    # filter(created_at__lte=timezone.now()).select_related("author").only/.defer("title")
    ofer = Oferta.objects.filter(created_at__lte=timezone.now()).select_related("author")
    
    #logger.debug("%d ofertas", len(ofer))

    return render(request, "oferta/index.html", {"oferta": ofer})


def oferta_detail(request, slug):
    oferta = get_object_or_404(Oferta, slug=slug)

    if request.user.is_active:
        if request.method == "POST":
            comentario_form = ComentarioForm(request.POST)
            
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)
                comentario.content_object = oferta
                comentario.creator = request.user
                comentario.save()
                return redirect(request.path_info)
        else:
            comentario_form = ComentarioForm()
    else:
        comentario_form = None
    
    return render(request, "oferta/oferta-detalhe.html", {"oferta": oferta, "comentario_form": comentario_form})