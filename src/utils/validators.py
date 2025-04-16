def validar_preco(preco):
    if not isinstance(preco, (int, float)):
        raise ValueError("O preço deve ser um número.")
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    return True

def validar_quantidade(quantidade):
    if not isinstance(quantidade, int):
        raise ValueError("A quantidade deve ser um número inteiro.")
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")
    return True

def validar_nome(nome):
    if not isinstance(nome, str):
        raise ValueError("O nome deve ser uma string.")
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    return True

def validar_descricao(descricao):
    if not isinstance(descricao, str):
        raise ValueError("A descrição deve ser uma string.")
    return True