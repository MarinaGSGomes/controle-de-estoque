import unittest
from models.produto import Produto, materiais_construcao

class TestProduto(unittest.TestCase):
    def test_adicionar_quantidade(self):
        produto = Produto(1, "Cimento", 25.50, 100, "Saco de cimento 50kg")
        produto.adicionar_quantidade(50)
        self.assertEqual(produto.quantidade, 150)

    def test_remover_quantidade(self):
        produto = Produto(1, "Cimento", 25.50, 100, "Saco de cimento 50kg")
        produto.remover_quantidade(50)
        self.assertEqual(produto.quantidade, 50)

    def test_remover_quantidade_invalida(self):
        produto = Produto(1, "Cimento", 25.50, 100, "Saco de cimento 50kg")
        with self.assertRaises(ValueError) as context:
            produto.remover_quantidade(150)
        self.assertEqual(str(context.exception), "Quantidade a ser removida é maior que a quantidade disponível.")

    def test_lista_materiais(self):
        self.assertEqual(len(materiais_construcao), 10)
        self.assertEqual(materiais_construcao[0].nome, "Cimento")

if __name__ == "__main__":
    unittest.main()