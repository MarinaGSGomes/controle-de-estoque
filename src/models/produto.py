class Produto:
    def __init__(self, id, nome, preco, quantidade, descricao):
        """Inicializa um produto com os atributos fornecidos."""
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao

    def __str__(self):
        """Retorna uma representação em string do produto."""
        return f"ID: {self.id}, Nome: {self.nome}, Preço: {self.preco:.2f}, Quantidade: {self.quantidade}, Descrição: {self.descricao}"

    def adicionar_quantidade(self, quantidade):
        """Adiciona uma quantidade ao estoque do produto."""
        if quantidade > 0:
            self.quantidade += quantidade
        else:
            raise ValueError("A quantidade a ser adicionada deve ser maior que zero.")

    def remover_quantidade(self, quantidade):
        """Remove uma quantidade do estoque do produto."""
        if quantidade > 0:
            if quantidade <= self.quantidade:
                self.quantidade -= quantidade
            else:
                raise ValueError("Quantidade a ser removida é maior que a quantidade disponível.")
        else:
            raise ValueError("A quantidade a ser removida deve ser maior que zero.")


# Lista de materiais de construção
materiais_construcao = [
    Produto(1, "Cimento", 25.50, 100, "Saco de cimento 50kg"),
    Produto(2, "Areia", 50.00, 200, "Metro cúbico de areia"),
    Produto(3, "Brita", 70.00, 150, "Metro cúbico de brita"),
    Produto(4, "Tijolo", 0.80, 1000, "Tijolo cerâmico 6 furos"),
    Produto(5, "Bloco de Concreto", 3.50, 500, "Bloco estrutural de concreto"),
    Produto(6, "Telha", 5.00, 300, "Telha cerâmica"),
    Produto(7, "Madeira", 120.00, 50, "Madeira serrada 3m"),
    Produto(8, "Prego", 15.00, 1000, "Caixa de pregos 1kg"),
    Produto(9, "Tubo PVC", 30.00, 100, "Tubo PVC 100mm"),
    Produto(10, "Ferro para Construção", 10.00, 500, "Barra de ferro 12mm"),
]