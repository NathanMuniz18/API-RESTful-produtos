from fastapi import FastAPI, HTTPException, status
from typing import List, Dict
from models import Produto
from database import db as product_db
print(">>> Rodando a API correta!")
app = FastAPI(
    title="API de Gerenciamento de Produtos",
    description="Uma API RESTful para realizar operações CRUD em produtos.",
    version="1.0.0",
)

@app.get("/", summary="Tela inicial da API")
def root():
    return {
        "mensagem": "🚀 Bem-vindo à API de Gerenciamento de Produtos!",
        "documentacao": "Acesse /docs para explorar os endpoints disponíveis.",
        "autor": "Nathan Viana"
    }
# Endpoint: Listar todos os produtost
@app.get("/produtos", response_model=List[Produto], summary="Lista todos os produtos disponíveis")
def read_all_products():
    """
    Retorna uma lista de todos os produtos no sistema.
    """
    # Usa o método listar_produtos() do seu objeto de banco de dados
    # Converte o dicionário de produtos em uma lista de objetos Produto
    return product_db.listar_produtos()

# Endpoint: Buscar produto por ID
@app.get("/produtos/{product_id}", response_model=Produto, summary="Busca um produto específico pelo ID")
def read_product_by_id(product_id: int):
    """
    Busca e retorna um produto com o ID especificado.
    Retorna 404 Not Found se o produto não for encontrado.
    """
    # Usa o método obter_produto() do seu objeto de banco de dados
    product = product_db.obter_produto(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto com ID {product_id} não encontrado")
    return product

# Endpoint: Criar novo produto
@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED, summary="Cria um novo produto")
def create_product(product: Produto):
    """
    Cria um novo produto no sistema com os dados fornecidos.
    O ID do produto será gerado automaticamente.
    """
    # Usa o método criar_produto() do seu objeto de banco de dados
    created_product = product_db.criar_produto(product)
    return created_product

# Endpoint: Atualizar produto existente
@app.put("/produtos/{product_id}", response_model=Produto, summary="Atualiza um produto existente pelo ID")
def update_existing_product(product_id: int, product: Produto):
    """
    Atualiza um produto existente com o ID especificado.
    Retorna 404 Not Found se o produto não for encontrado.
    """
    # Garante que o ID do produto no corpo da requisição corresponda ao ID da URL, se for fornecido
    if product.id is not None and product.id != product_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID do produto no corpo não corresponde ao ID da URL")

    # Usa o método atualizar_produto() do seu objeto de banco de dados
    updated_product = product_db.atualizar_produto(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto com ID {product_id} não encontrado")
    return updated_product

# Endpoint: Remover produto
@app.delete("/produtos/{product_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Remove um produto pelo ID")
def delete_product(product_id: int):
    """
    Remove um produto com o ID especificado.
    Retorna 404 Not Found se o produto não for encontrado.
    """
    # Usa o método remover_produto() do seu objeto de banco de dados
    if not product_db.remover_produto(product_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto com ID {product_id} não encontrado")
    return {"message": "Produto removido com sucesso"} # FastAPI retornará 204 No Content para isso