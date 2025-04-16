import unittest
from src.models.produto import Produto
from src.services.estoque import EstoqueService

class TestEstoqueService(unittest.TestCase):

    def setUp(self):
        self.estoque_service = EstoqueService()
        self.produto = Produto(id=1, nome="Produto Teste", preco=10.0, quantidade=100, descricao="Descrição do produto teste")
        self.estoque_service.adicionar_produto(self.produto)

    def test_listar_produtos(self):
        produtos = self.estoque_service.listar_produtos()
        self.assertIn(self.produto, produtos)

    def test_buscar_produto_por_id(self):
        produto_encontrado = self.estoque_service.buscar_produto_por_id(1)
        self.assertEqual(produto_encontrado.id, self.produto.id)

    def test_atualizar_produto(self):
        self.produto.preco = 12.0
        self.estoque_service.atualizar_produto(self.produto)
        produto_atualizado = self.estoque_service.buscar_produto_por_id(1)
        self.assertEqual(produto_atualizado.preco, 12.0)

    def tearDown(self):
        self.estoque_service.remover_produto(1)

if __name__ == '__main__':
    unittest.main()