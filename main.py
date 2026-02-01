from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra
from modelos.gestor import Gerenciador

def main():
    gerenciador = Gerenciador()

    print("=== TESTE: ADICIONAR ITEM ===")
    item = gerenciador.adicionar_novo_item()

    print("\n=== ITEM CRIADO ===")
    print(f"Produto: {item.produto.nome_produto}")
    print(f"Código: {item.produto.codigo}")
    print(f"Marca: {item.produto.nome_marca}")
    print(f"Valor unitário: R$ {item.valor_unitario}")
    print(f"Quantidade: {item.quantidade}")

    print("\n=== PRODUTOS CADASTRADOS ===")
    for produto in gerenciador.produtos_cadastrados:
        print(f"- {produto.codigo} | {produto.nome_produto} ({produto.nome_marca})")

if __name__ == "__main__":
    main()
