class SaidaService:
    def __init__(self, estoque_service):
        self.estoque_service = estoque_service

    def registrar_saida(self, produto_id, quantidade):
        produto = self.estoque_service.buscar_produto_por_id(produto_id)
        if produto is None:
            raise ValueError("Produto não encontrado.")
        if quantidade > produto.quantidade:
            raise ValueError("Quantidade solicitada maior do que a disponível.")
        
        produto.remover_quantidade(quantidade)
        return produto.quantidade  # Retorna a nova quantidade após a saída.