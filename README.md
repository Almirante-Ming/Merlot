prototipo para filtragem e envio de mensagens.

para executar:

    pip install poetry poetry-plugin-shell

abra a raiz do projeto:

    poetry shell

    poetry install

    task run



estrutura modelo do flask:


project/
│
├── app/                     # Diretório principal da aplicação
│   ├── __init__.py          # Inicialização da aplicação (Factory App)
│   ├── models.py            # Modelos do banco de dados
│   ├── routes.py            # Rotas e controladores
│   ├── templates/           # Arquivos HTML (Jinja templates)
│   ├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── forms.py             # Definição de formulários
│   └── utils.py             # Funções utilitárias
│
├── migrations/              # Arquivos de migração (Alembic)
│
├── tests/                   # Testes da aplicação
│   ├── test_app.py          # Testes unitários
│
├── instance/                # Configurações específicas de ambiente
│   └── config.py            # Arquivo de configuração (Ex.: desenvolvimento, produção)
│
├── pyproject.toml           # Arquivo de configuração do Poetry
├── README.md                # Documentação do projeto
├── .gitignore               # Arquivos ignorados pelo Git
└── run.py                   # Script para executar a aplicação
