from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra
from modelos.gestor import Gerenciador

from modelos.gestor import Gerenciador

def main():
    gestor = Gerenciador()
    
    print("=== TESTE DE COMPRA ===")
    gestor.adicionar_nova_compra()
    
    # Mostrar resumo das compras
    print("\n=== COMPRAS REGISTRADAS ===")
    for compra in gestor.compras_cadastradas:
        print(compra)

if __name__ == "__main__":
    main()
