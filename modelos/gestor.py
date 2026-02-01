from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

class Gerenciador:
    def __init__(self):
        self.produtos_cadastrados = []
        self.itens_cadastrados = []

        p1 = Produto("1", "Arroz", "Marca X", "kg", "5")
        p2 = Produto("2", "Feijão", "Marca Y", "kg", "1")
        
        self.produtos_cadastrados.append(p1)
        self.produtos_cadastrados.append(p2)

        self.compra_atual = None

    def adicionar_nova_compra(self):
        pass
        #pede o nome do mercado
        #pede a data da compra
        # cria uma lista de item vazia
        #chama a def adicionar_novo_item() conforme o usuario e adiciona o retorno dela para a lista criada acima
        # calcula total da compra chamando a funcao calcular funcao compra da classe compra
        # retorna nova compra

    def adicionar_novo_item(self):
        codigo = int(input('Digite o codigo de barras: '))
        produto = self.buscar_produto(codigo)
        if produto is None:
            produto = self.adicionar_novo_produto(codigo)
        valor_unitario = float(input('Digite o valor do item R$: '))
        quantidade = int(input('Digite a quantidade: '))
        item = Item(produto, valor_unitario, quantidade)
        return item

    def adicionar_novo_produto(self, codigo):
        nome_produto = str(input('Digite o nome do produto: '))
        nome_marca = str(input('Digite o nome da marca: '))
        unidade_medida = str(input('Digite a unidade de medida: '))
        qtd_unidade = float(input(f'Quanto(s) {unidade_medida}: '))
        produto = Produto(codigo, nome_produto, nome_marca, unidade_medida, qtd_unidade)
        self.produtos_cadastrados.append(produto)
        return produto
    
    def buscar_produto(self, codigo):
        for produto in self.produtos_cadastrados:
            if produto.codigo == codigo:
                return produto
        return None
