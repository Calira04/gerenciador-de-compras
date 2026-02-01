from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra
from modelos.gestor import Gerenciador

ger = Gerenciador()

codigo_teste = 3
resultado = ger.buscar_produto(codigo_teste)

print(resultado)
