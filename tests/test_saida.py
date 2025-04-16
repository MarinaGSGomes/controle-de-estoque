import unittest
from src.models.produto import Produto
from src.services.saida import SaidaService

class TestSaidaService(unittest.TestCase):

    def setUp(self):
        self.produto = Produto(id=1, nome="Produto Teste", preco=10.0, quantidade=5, descricao="Descrição do produto teste")
        self.saida_service = SaidaService()

    def test_registrar_saida_com_sucesso(self):
        quantidade_saida = 2
        self.saida_service.registrar_saida(self.produto, quantidade_saida)
        self.assertEqual(self.produto.quantidade, 3)

    def test_registrar_saida_quantidade_insuficiente(self):
        quantidade_saida = 6
        with self.assertRaises(ValueError):
            self.saida_service.registrar_saida(self.produto, quantidade_saida)

    def test_registrar_saida_quantidade_zero(self):
        quantidade_saida = 0
        with self.assertRaises(ValueError):
            self.saida_service.registrar_saida(self.produto, quantidade_saida)

if __name__ == '__main__':
    unittest.main()