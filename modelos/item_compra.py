from modelos.produto import Produto


class Item:
    '''
    Representa um item de uma compra.

    Um item associa um produto a um valor unitário e a uma quantidade,
    permitindo calcular o subtotal daquele produto na compra.
    '''

    def __init__(self, produto, valor_unitario, quantidade):
        '''
        Inicializa um novo item de compra.

        Args:
            produto (Produto): Objeto Produto associado ao item.
            valor_unitario (float): Preço de uma unidade do produto.
            quantidade (int): Quantidade de unidades compradas.
        '''

        # Produto associado ao item
        self.produto = produto

        # Valor unitário do produto
        self.valor_unitario = float(valor_unitario)

        # Quantidade comprada
        self.quantidade = int(quantidade)

    def calcular_total(self):
        '''
        Calcula o valor total do item (subtotal).

        Returns:
            float: Valor total do item.
        '''
        return self.valor_unitario * self.quantidade

    def __str__(self):
        '''
        Retorna uma representação em texto do item.

        Returns:
            str: Informações do item formatadas em uma única linha.
        '''
        return (
            f'{self.produto.nome_produto} | '
            f'{self.valor_unitario:.2f} | '
            f'{self.quantidade} | '
            f'Subtotal: {self.calcular_total():.2f}'
        )
