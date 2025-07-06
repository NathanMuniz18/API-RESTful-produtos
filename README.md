
#  API de Gerenciamento de Produtos

Uma API RESTful simples desenvolvida com **FastAPI** para realizar operações de **CRUD** (Create, Read, Update, Delete) sobre uma entidade fictícia de **produto**.

##  Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn (servidor ASGI)

##  Funcionalidades

A API permite:

- Listar todos os produtos (`GET /produtos`)
-  Buscar um produto por ID (`GET /produtos/{id}`)
-  Criar um novo produto (`POST /produtos`)
-  Atualizar um produto existente (`PUT /produtos/{id}`)
-  Remover um produto (`DELETE /produtos/{id}`)

##  Modelo de Produto

```json
{
  "nome": "Smartphone",
  "descricao": "Um smartphone avançado",
  "preco": 1999.99,
  "quantidade": 50
}
```

> O campo `id` é gerado automaticamente.

##  Como Rodar Localmente

1. **Clone o repositório**:
```bash
git clone https://github.com/NathanMuniz18/API-RESTful-produtos.git
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instale as dependências**:
```bash
pip install fastapi uvicorn
```

4. **Inicie o servidor**:
```bash
uvicorn main:app --reload
```

5. **Acesse a documentação interativa**:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- os testes podem ser feitos usando o Swagger ui e depois so usar a url gerada para redirecionar e ver o que aconteceu

##  Observação

> Esta aplicação utiliza **banco de dados em memória**, ou seja, os dados são **apagados a cada reinicialização**.

##  Autor

- Nathan Viana
- https://github.com/NathanMuniz18
