class EntradaService:
    def __init__(self, estoque_service):
        self.estoque_service = estoque_service

    def registrar_entrada(self, produto_id, quantidade):
        produto = self.estoque_service.buscar_produto_por_id(produto_id)
        if produto:
            produto.adicionar_quantidade(quantidade)
            return True
        return False