from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import ProdutoModel
from django.urls import reverse_lazy

 
class ProdutoUpdateView(UpdateView):
    # specify the model you want to use
    model = ProdutoModel
 
    # specify the fields
    fields = [
        "nome",
        "quantidade"
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('produtos')

 
class ProdutoList(ListView):
    model = ProdutoModel
 
class ProdutoCreate(CreateView):
    model = ProdutoModel
    #template_name = 'produto/produtomodel_form.html'
    fields = ['nome', 'quantidade']
    success_url = reverse_lazy('produtos')
