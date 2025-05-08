prototipo para filtragem e envio de mensagens.

abra a raiz do projeto:

pip install .

tasak tun



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
-------------------------------------------------------------------
# Projeto de Envio de Mensagens via WhatsApp com Twilio

Este projeto permite o envio de mensagens via WhatsApp utilizando o Twilio, integrado com o Flask para criar um servidor simples. O código carrega variáveis de ambiente de um arquivo `.env` para garantir que as credenciais não sejam expostas no código-fonte.

## Estrutura do Projeto

1. **main.py** - Arquivo principal que configura o Flask e a rota para enviar mensagens.
2. **whatsapp.py** - Contém a função para enviar mensagens usando a API do Twilio.
3. **.env** - Arquivo de variáveis de ambiente com as credenciais do Twilio.
4. **requirements.txt** - Lista de dependências do projeto.
5. **README.md** - Este arquivo de documentação.

## Passos para Execução

### 1. Clonar o Repositório

Clone o repositório utilizando o comando:

```bash
git clone https://github.com/usuario/repositorio.git
-----------------------------------------------------------------------
### Configurar o Twilio
Para configurar o Twilio, siga os passos abaixo:

Crie uma conta no Twilio.

Ative o WhatsApp Sandbox no painel do Twilio.

Pegue as credenciais (Account SID, Auth Token) e o número de telefone do Sandbox do Twilio.
