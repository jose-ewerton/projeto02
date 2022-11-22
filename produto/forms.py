
from django import forms
from .models import ProdutoModel
 
 
# creating a form
class ProdutoForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ProdutoModel
 
        # specify fields to be used
        fields = [
            "nome",
            "quantidade",
        ]