class EstoqueService:
    def __init__(self):
        self.produtos = []

    def listar_produtos(self):
        return self.produtos

    def buscar_produto_por_id(self, produto_id):
        for produto in self.produtos:
            if produto.id == produto_id:
                return produto
        return None

    def atualizar_produto(self, produto_id, nome=None, preco=None, quantidade=None, descricao=None):
        produto = self.buscar_produto_por_id(produto_id)
        if produto:
            if nome is not None:
                produto.nome = nome
            if preco is not None:
                produto.preco = preco
            if quantidade is not None:
                produto.quantidade = quantidade
            if descricao is not None:
                produto.descricao = descricao
            return True
        return False

    def adicionar_produto(self, produto):
        self.produtos.append(produto)