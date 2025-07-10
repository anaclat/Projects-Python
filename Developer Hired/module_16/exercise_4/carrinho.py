from time import sleep
total_arrinho = 0

class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self,produto):
        self.produtos.append(produto)

    def finalizar_pedido(self):
        print(f'Finalizando o seu pedido...')
        sleep(2)
        print(f'Você possui {len(self.produtos)} produtos no carrinho.')
        
        total_carrinho = 0

        for produto in self.produtos:
            print(f'Você pediu 1 {produto.nome} com os sabores:')

            for sabor in produto.sabores:
                print(f' - {sabor}')

            total_carrinho += produto.preco

        print(f'VALOR À PAGAR: R$ {total_carrinho}')