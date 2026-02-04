from datetime import datetime
from modelos.produto import Produto
from modelos.item_compra import Item
from modelos.compra import Compra

caminho_produtos = 'data/produtos.txt'
caminho_compras = 'data/compras.txt'

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
        self.carregar_produtos()

    def solicitar_codigo_barras(self):
        while True:
            codigo = input('Digite o código de barras: ').strip()

            # campo vazio
            if not codigo:
                print('Código vazio. Digite novamente.')
                continue

            # só dígitos
            if not codigo.isdigit():
                print('Código inválido. Use apenas números.')
                continue

            # regra de domínio (exemplo)
            if len(codigo) < 4:
                print('Código muito curto. Digite novamente.')
                continue

            # passou por todas as validações
            return codigo
        
    def solicitar_nome(self, rotulo):
        while True:
            nome = input(f'Digite o nome do {rotulo}: ').strip()

            # campo vazio
            if not nome:
                print(f'O nome do {rotulo} não pode ser vazio.')
                continue

            # normalização simples (opcional, mas recomendada)
            nome = nome.upper()

            return nome
    
    def solicitar_float(self, rotulo):
        while True:
            valor = input(f'Digite o {rotulo}: ').strip()

            if not valor:
                print(f'O {rotulo} não pode ser vazio.')
                continue

            # aceita vírgula como separador decimal
            valor = valor.replace(',', '.')

            try:
                valor = float(valor)
            except ValueError:
                print(f'Valor inválido para {rotulo}. Digite um número.')
                continue

            if valor < 0:
                print(f'O {rotulo} não pode ser negativo.')
                continue

            return valor

    from datetime import datetime

    def solicitar_data(self, rotulo):
        while True:
            data_txt = input(f'Digite a {rotulo} (dd/mm/aaaa): ').strip()

            if not data_txt:
                print(f'A {rotulo} não pode ser vazia.')
                continue

            try:
                data = datetime.strptime(data_txt, '%d/%m/%Y').date()
            except ValueError:
                print('Data inválida. Use o formato dd/mm/aaaa.')
                continue

            return data

    def adicionar_nova_compra(self):
        '''
        Cria uma nova compra, adiciona itens e guarda no histórico.
        '''
        nome_mercado = self.solicitar_nome('mercado')
        data_compra = self.solicitar_data('data da compra')
        
        compra_atual = Compra(nome_mercado, data_compra)
        
        while True:
            opcao = input("\nDigite 'sair' para finalizar ou qualquer tecla para adicionar item: ").lower()
            if opcao == 'sair':
                break
            
            item = self.adicionar_novo_item()
            compra_atual.adicionar_item(item)
            
            print(f'Total acumulado: R$ {compra_atual.calcular_total_compra():.2f}')

        self.compras_cadastradas.append(compra_atual)
        self.salvar_compras()

        print('\n--- COMPRA SALVA COM SUCESSO ---')

    def adicionar_novo_item(self):
        '''
        Solicita dados do item e cria um Item associado a um Produto.
        '''
        codigo = self.solicitar_codigo_barras()
        produto = self.buscar_produto(codigo)
        
        if produto is None:
            produto = self.adicionar_novo_produto(codigo)
        
        valor_unitario = self.solicitar_float('valor do item (R$)')
        quantidade = self.solicitar_float('quantidade')
        
        item = Item(produto, valor_unitario, quantidade)
        
        print('\nItem adicionado:')
        print(item)
        
        return item

    def adicionar_novo_produto(self, codigo):
        '''
        Cria um novo produto e adiciona à lista de produtos cadastrados.
        '''
        nome_produto = self.solicitar_nome('produto')
        nome_marca = self.solicitar_nome('marca')
        unidade_medida = self.solicitar_nome('unidade de medida (L, ML, KG, G)')
        qtd_unidade = self.solicitar_float('quantidade em (L, ML, KG, G)')
        
        produto = Produto(codigo, nome_produto, nome_marca, unidade_medida, qtd_unidade)
        self.produtos_cadastrados.append(produto)

        self.salvar_produtos()
        
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

    def carregar_produtos(self):
        with open(caminho_produtos, 'r') as arquivo:
            for linha in arquivo:
                codigo, nome, marca, unidade, qtd = linha.strip().split(',')
                produto = Produto(codigo, nome, marca, unidade, float(qtd))
                self.produtos_cadastrados.append(produto)
    
    def salvar_produtos(self):
        with open(caminho_produtos, 'w') as arquivo:
            for produto in self.produtos_cadastrados:
                arquivo.write(f'{produto.codigo},{produto.nome_produto},{produto.nome_marca},{produto.unidade_medida},{produto.qtd_unidade}\n')
    
    def carregar_compras(self):
        with open(caminho_compras, 'r') as arquivo:
            next(arquivo)  # pula o cabeçalho
            compras_dict = {}  # para agrupar itens pela mesma compra
            
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                
                data, mercado, codigo, nome, marca, unidade_medida, qtd_medida, quantidade, valor_unitario, valor_total = linha.split(',')
                
                codigo = codigo
                qtd_medida = float(qtd_medida)
                quantidade = float(quantidade)
                valor_unitario = float(valor_unitario)
                
                # recria o produto e o item
                produto = Produto(codigo, nome, marca, unidade_medida, qtd_medida)
                item = Item(produto, valor_unitario, quantidade)
                
                # chave única para agrupar itens da mesma compra
                chave = (data, mercado)
                if chave not in compras_dict:
                    compras_dict[chave] = Compra(mercado, data)
                
                compras_dict[chave].adicionar_item(item)
            
            # adiciona todas as compras ao histórico do Gestor
            self.compras_cadastradas = list(compras_dict.values())

    def salvar_compras(self):
        with open(caminho_compras, 'w') as arquivo:
            # percorre todas as compras
            for compra in self.compras_cadastradas:
                for item in compra.itens:
                    produto = item.produto
                    # escreve os dados no formato CSV
                    arquivo.write(f'{compra.data_compra},{compra.nome_mercado},{produto.codigo},{produto.nome_produto},'
                                f'{produto.nome_marca},{produto.unidade_medida},{produto.qtd_unidade},{item.quantidade},'
                                f'{item.valor_unitario},{item.calcular_total():.2f}\n')
        