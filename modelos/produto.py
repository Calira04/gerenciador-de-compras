class Produto:
    """
    Representa um produto cadastrado no sistema.

    Um produto contém informações básicas que não mudam com a compra,
    como código, nome, marca e unidade de medida.
    """

    def __init__(self, codigo, nome_produto, nome_marca, unidade_medida, qtd_unidade):
        """
        Inicializa um novo objeto Produto.

        Args:
            codigo (int): Código identificador do produto.
            nome_produto (str): Nome do produto.
            nome_marca (str): Marca do produto.
            unidade_medida (str): Unidade de medida (ex: kg, un, L).
            qtd_unidade (float): Quantidade correspondente à unidade de medida.
        """

        # Código do produto (convertido para inteiro)
        self.codigo = int(codigo)

        # Nome do produto
        self.nome_produto = str(nome_produto)

        # Marca do produto
        self.nome_marca = str(nome_marca)

        # Unidade de medida do produto (ex: kg, unidade, litro)
        self.unidade_medida = str(unidade_medida)

        # Quantidade referente à unidade de medida
        self.qtd_unidade = float(qtd_unidade)

    def __str__(self):
        """
        Retorna uma representação em texto do produto.

        Returns:
            str: Informações do produto formatadas em uma única linha.
        """
        return (
            f'{self.codigo} | '
            f'{self.nome_produto} | ' 
            f'{self.nome_marca} | '
            f'{self.unidade_medida} | '
            f'{self.qtd_unidade}'
        )