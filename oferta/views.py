from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy, reverse

from oferta.models import Oferta, Investimento
from oferta.forms import ComentarioForm, InvestimentoForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def index(request):
    # filter(created_at__lte=timezone.now()).select_related("author").only/.defer("title")
    ofer = Oferta.objects.filter(created_at__lte=timezone.now()).select_related("author")
    
    #logger.debug("%d ofertas", len(ofer))

    return render(request, "oferta/index.html", {"oferta": ofer})

class OfertaList(ListView):
    model = Oferta
    template_name = 'oferta/listar.html'
    context_object_name = 'oferta'

class OfertaCreate(CreateView):
    model = Oferta
    template_name = 'oferta/registrar.html'
    fields = '__all__'
    context_object_name = 'oferta'
    success_url = reverse_lazy('oferta')

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        #form.instance.img = self.request.FILES
        
        return super(OfertaCreate, self).form_valid(form)

class OfertaUpdate(UpdateView):
    model = Oferta
    template_name = 'oferta/registrar.html'
    context_object_name = 'oferta'
    fields = '__all__'
    success_url = reverse_lazy('oferta')

class OfertaDelete(DeleteView):
    model = Oferta
    template_name = 'ofertar/deletar.html'
    context_object_name = 'oferta'
    success_url = reverse_lazy('oferta')

class OfertaDetail(FormMixin, DetailView):
    model = Oferta
    template_name = 'oferta/detalhes.html' 
    form_class = ComentarioForm

    def post(self, request, *args, **kwargs):
        comentario_form = self.get_form()
        self.object = self.get_object()
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.content_object = self.object
            comentario.creator_comment = self.request.user
            comentario.save()
            return redirect(request.path_info)
        else:
            return self.form_invalid(comentario_form)

class InvestimentoView(FormMixin, DetailView):
    model = Oferta
    template_name = 'oferta/oferta-detalhe.html'
    #context_object_name = 'oferta'
    form_class = InvestimentoForm

    def post(self, request, *args, **kwargs):
        investimento_form = self.get_form()
        self.object = self.get_object()
        if investimento_form.is_valid():
            investimento = investimento_form.save(commit=False)
            investimento.content_object = self.object
            investimento.creator_invest = self.request.user
            investimento.save()
            return redirect(request.path_info)
        else:
            return self.form_invalid(investimento_form)


class InvestimentoListView(ListView):
    #model = Investimento
    queryset = Investimento.objects.all()
    template_name = 'oferta/listar-investimento.html'
    context_object_name = 'investimento'
