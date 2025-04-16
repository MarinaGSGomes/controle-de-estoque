import unittest
from src.models.produto import Produto
from src.services.entrada import EntradaService

class TestEntradaService(unittest.TestCase):
    def setUp(self):
        self.produto = Produto(id=1, nome="Produto Teste", preco=10.0, quantidade=5, descricao="Descrição do produto teste")
        self.entrada_service = EntradaService()

    def test_registrar_entrada(self):
        quantidade_inicial = self.produto.quantidade
        quantidade_adicionada = 10
        self.entrada_service.registrar_entrada(self.produto, quantidade_adicionada)
        self.assertEqual(self.produto.quantidade, quantidade_inicial + quantidade_adicionada)

    def test_registrar_entrada_zero(self):
        quantidade_inicial = self.produto.quantidade
        quantidade_adicionada = 0
        self.entrada_service.registrar_entrada(self.produto, quantidade_adicionada)
        self.assertEqual(self.produto.quantidade, quantidade_inicial)

    def test_registrar_entrada_negativa(self):
        quantidade_inicial = self.produto.quantidade
        quantidade_adicionada = -5
        with self.assertRaises(ValueError):
            self.entrada_service.registrar_entrada(self.produto, quantidade_adicionada)

if __name__ == '__main__':
    unittest.main()