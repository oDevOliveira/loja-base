# LojaBase

E-commerce desenvolvido com Python e Flask, com catálogo de produtos, carrinho de compras, autenticação de usuários, painel administrativo e integração de pagamentos via Asaas.

## Funcionalidades

- Cadastro e login de usuários.
- Catálogo de produtos com categorias.
- Consulta de detalhes dos produtos.
- Carrinho de compras com seleção de quantidades.
- Criação e acompanhamento de pedidos.
- Integração com a API de pagamentos Asaas.
- Geração de cobranças por boleto bancário.
- Armazenamento do link de pagamento dos pedidos.
- Painel administrativo com acesso restrito a administradores.
- Gerenciamento de produtos e pedidos.

## Tecnologias utilizadas

- **Python** — linguagem principal.
- **Flask** — framework web.
- **Flask-SQLAlchemy** — integração com o banco de dados.
- **Flask-Login** — autenticação e gerenciamento de sessões.
- **SQLite** — banco de dados.
- **HTML e CSS** — estrutura e estilização das páginas.
- **Asaas API** — integração com pagamentos.

## Estrutura do projeto

```text
LojaBase/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── decorators.py
│   ├── routes/
│   │   ├── loja.py
│   │   ├── catalogo.py
│   │   ├── carrinho.py
│   │   ├── pagamento.py
│   │   ├── autenticacao.py
│   │   └── dashboard.py
│   ├── services/
│   ├── templates/
│   └── static/
│       └── img/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

*Estrutura ilustrativa: os nomes e diretórios devem corresponder aos arquivos existentes no projeto.*

## Como executar

### 1. Pré-requisitos

- Python instalado.
- Git (opcional).
- Conta no Asaas para testar a integração de pagamentos.

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd LojaBase
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure a integração de pagamentos

Configure no arquivo de configuração do projeto as credenciais necessárias para a API do Asaas.

Utilize credenciais de teste durante o desenvolvimento e não publique chaves privadas no GitHub.

### 6. Execute a aplicação

```bash
python run.py
```

Acesse no navegador o endereço local informado pelo Flask, normalmente:

```text
http://127.0.0.1:5000/
```

## Segurança

- As senhas dos usuários devem ser armazenadas com hash.
- As rotas administrativas devem verificar as permissões do usuário.
- As credenciais da API de pagamentos não devem ser expostas publicamente.
- A validação de estoque e quantidade deve ocorrer no servidor.
- Os dados de pagamento devem ser tratados conforme as regras da API do Asaas.

## Objetivo

O LojaBase é um projeto de desenvolvimento web voltado à prática de Python, Flask, banco de dados relacionais, autenticação, controle de acesso e integração com serviços externos de pagamento.

## Status

Em desenvolvimento.