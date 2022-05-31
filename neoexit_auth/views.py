from django.shortcuts import render

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from oferta.models import Investimento, Oferta

@login_required
def perfil(request):
    #investimento = Investimento.objects.all()

    o = Oferta.objects.first()
    investimento = o.investimentos.all()
    #post_type = ContentType.objects.get_for_model(Post)
    #Comment.objects.update(content_type=post_type)
    #investimento = Investimento.objects.filter(content_types=ct, object_id=o.pk)
    #investimento = ContentType.objects.get(app_label="oferta", model="investimento")
    #investimento = ContentType.objects.get_for_model(Investimento)

    return render(request, "neoexit_auth/perfil.html", {"investimento": investimento})

