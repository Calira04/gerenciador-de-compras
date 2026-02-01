from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

class Gerenciador:
    '''
    Classe para gerenciar produtos e compras.
    '''

    def __init__(self):
        '''
        Inicializa o gerenciador com listas de produtos e compras.
        '''
        self.produtos_cadastrados = []
        self.compras_cadastradas = []

    def adicionar_nova_compra(self):
        '''
        Cria uma nova compra, adiciona itens e guarda no histórico.
        '''
        nome_mercado = input('Digite o nome do mercado: ')
        data_compra = input('Digite a data da compra: ')
        
        compra_atual = Compra(nome_mercado, data_compra)
        
        while True:
            opcao = input("\nDigite 'sair' para finalizar ou qualquer tecla para adicionar item: ").lower()
            if opcao == 'sair':
                break
            
            item = self.adicionar_novo_item()
            compra_atual.adicionar_item(item)
            
            print(f'Total acumulado: R$ {compra_atual.calcular_total_compra():.2f}')

        self.compras_cadastradas.append(compra_atual)
        print('\n--- COMPRA SALVA COM SUCESSO ---')

    def adicionar_novo_item(self):
        '''
        Solicita dados do item e cria um Item associado a um Produto.
        '''
        codigo = int(input('Digite o código de barras: '))
        produto = self.buscar_produto(codigo)
        
        if produto is None:
            produto = self.adicionar_novo_produto(codigo)
        
        valor_unitario = float(input('Digite o valor do item R$: '))
        quantidade = int(input('Digite a quantidade: '))
        
        item = Item(produto, valor_unitario, quantidade)
        
        print('\nItem adicionado:')
        print(item)
        
        return item

    def adicionar_novo_produto(self, codigo):
        '''
        Cria um novo produto e adiciona à lista de produtos cadastrados.
        '''
        nome_produto = input('Digite o nome do produto: ')
        nome_marca = input('Digite o nome da marca: ')
        unidade_medida = input('Digite a unidade de medida: ')
        qtd_unidade = float(input(f'Quanto(s) {unidade_medida}: '))
        
        produto = Produto(codigo, nome_produto, nome_marca, unidade_medida, qtd_unidade)
        self.produtos_cadastrados.append(produto)
        
        return produto
    
    def buscar_produto(self, codigo):
        '''
        Busca um produto pelo código de barras.
        Retorna o Produto ou None se não existir.
        '''
        for produto in self.produtos_cadastrados:
            if produto.codigo == codigo:
                return produto
        return None
