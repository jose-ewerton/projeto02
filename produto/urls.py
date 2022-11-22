from django.urls import path
from .views import ProdutoCreate, ProdutoList, ProdutoUpdateView

urlpatterns = [
    path('criar/', ProdutoCreate.as_view(), name= 'criar-produto' ),
    path('', ProdutoList.as_view(), name= 'produtos' ),
    path('comprar/<int:pk>', ProdutoUpdateView.as_view(), name= 'comprar-produto'),
]