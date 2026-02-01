from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

class Gerenciador:
    def __init__(self):
        self.produtos_cadastrados = []

        p1 = Produto("1", "Arroz", "Marca X", "kg", "5")
        p2 = Produto("2", "Feijão", "Marca Y", "kg", "1")
        
        self.produtos_cadastradis.append(p1)
        self.produtos_cadastradis.append(p2)

        self.compra_atual = None

    def adicionar_nova_compra(self):
        #pede o nome do mercado
        #pede a data da compra
        # cria uma lista de item vazia
        #chama a def adicionar_novo_item() conforme o usuario e adiciona o retorno dela para a lista criada acima
        # calcula total da compra chamando a funcao calcular funcao compra da classe compra
        # retorna nova compra

    def adicionar_novo_item(self):
        #pede o codigo de barras
        #chama a funcao buscar item
        #se a funcao buscar item retornar verdadeiro puxe o valores dos produto dela e pule adicionar novo produto
        #se falso chame adicionar novo produto
        #adiciona o valor
        #adiciona preco
        #puxa funcao da classe item com valor total
        #retorna novo item


    def adicionar_novo_produto(self):
        #ele recebe novo codigo de barra
        #verifica funcao buscar produto
        #se verdadeira retorna valores do produto
        #se falsa pede restante dos dados pra catalogar produto e retorna novo produto     

    def buscar_produto(self):
        #recebe o codigo de barra novo
        #verifica se ele ja existe
        #se sim retorna valores do produto
        #se nao retorna falso