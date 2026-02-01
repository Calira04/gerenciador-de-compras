from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

# Produtos
p1 = Produto("1", "Arroz", "Marca X", "kg", 5)
p2 = Produto("2", "Feijão", "Marca Y", "kg", 1)

# Compra
minha_compra = Compra("31/01/2026", "Mercado Central")

# Adicionando Itens
minha_compra.adicionar_item(Item(p1, 25.00, 2)) # 2 pacotes de arroz
minha_compra.adicionar_item(Item(p2, 8.50, 3))  # 3 pacotes de feijão

# O GRANDE FINAL
print(minha_compra)