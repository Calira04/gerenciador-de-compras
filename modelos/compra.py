from modelos.produto import Produto
from modelos.item_compra import Item


class Compra:
    '''
    Representa uma compra realizada em um mercado.

    Uma compra possui um nome de mercado, uma data e uma lista de itens.
    Cada item corresponde a um produto comprado com quantidade e valor.
    '''

    def __init__(self, nome_mercado, data_compra):
        '''
        Inicializa uma nova compra.

        Args:
            nome_mercado (str): Nome do mercado onde a compra foi realizada.
            data_compra (str): Data em que a compra ocorreu.
        '''

        # Nome do mercado
        self.nome_mercado = nome_mercado

        # Data da compra
        self.data_compra = data_compra

        # Lista de itens da compra
        self.itens = []

    def adicionar_item(self, item):
        '''
        Adiciona um item à lista de itens da compra.

        Args:
            item (Item): Objeto Item a ser adicionado à compra.
        '''
        self.itens.append(item)

    def calcular_total_compra(self):
        '''
        Calcula o valor total da compra somando o subtotal de cada item.

        Returns:
            float: Valor total da compra.
        '''
        total_geral = 0

        for item in self.itens:
            total_geral += item.calcular_total()

        return total_geral

    def __str__(self):
        '''
        Retorna uma representação em texto da compra completa.

        Inclui:
        - Cabeçalho com mercado e data
        - Lista de itens
        - Total da compra

        Returns:
            str: Compra formatada em múltiplas linhas.
        '''

        # Cabeçalho da compra
        cabecalho = f'--- COMPRA: {self.nome_mercado} ({self.data_compra}) ---\n'

        # Corpo com a lista de itens (cada item em uma linha)
        corpo_itens = '\n'.join([str(item) for item in self.itens])

        # Rodapé com o total da compra
        rodape = '\n------------------------------------------'
        rodape += f'\nTOTAL DA COMPRA: R$ {self.calcular_total_compra():.2f}'

        return cabecalho + corpo_itens + rodape
