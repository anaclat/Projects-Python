from produto import Produto
from carrinho import Carrinho

pastel = Produto(nome='Pastel',preco=15.50,tamanho='Pequeno',sabores=['carne','queijo'])
coca = Produto(nome='Coca Cola',preco=9.50,tamanho='2L',sabores=['zero'])

carrinho = Carrinho()
carrinho.adicionar_produto(pastel)
carrinho.adicionar_produto(coca)

carrinho.finalizar_pedido()