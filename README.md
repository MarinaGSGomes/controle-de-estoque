# Controle de Estoque

Este projeto é um sistema de controle de estoque que permite gerenciar a entrada e saída de produtos. O sistema é estruturado em várias camadas, seguindo boas práticas de programação em Python.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
controle-estoque
├── src
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── models
│   │   └── produto.py         # Definição da classe Produto
│   ├── services
│   │   ├── entrada.py         # Lógica de entrada de produtos
│   │   ├── saida.py           # Lógica de saída de produtos
│   │   └── estoque.py         # Gestão do estoque
│   ├── utils
│   │   └── validators.py      # Funções de validação
│   └── database
│       └── db_connection.py   # Gerenciamento da conexão com o banco de dados
├── tests
│   ├── test_entrada.py        # Testes para a classe EntradaService
│   ├── test_saida.py          # Testes para a classe SaidaService
│   └── test_estoque.py        # Testes para a classe EstoqueService
├── requirements.txt           # Dependências do projeto
├── .gitignore                 # Arquivos a serem ignorados pelo Git
└── README.md                  # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar o sistema de controle de estoque, execute o arquivo `main.py`:

```
python src/main.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.