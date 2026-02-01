from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

class Gerenciador:
    def __init__(self):
        self.produtos_cadastradis = []

        p1 = Produto("1", "Arroz", "Marca X", "kg", "5")
        p2 = Produto("2", "Feijão", "Marca Y", "kg", "1")
        
        self.produtos_cadastradis.append(p1)
        self.produtos_cadastradis.append(p2)

        self.compra_atual = None