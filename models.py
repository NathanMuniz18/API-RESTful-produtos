from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None  # Gerado automaticamente, por isso Optional
    nome: str
    descricao: str
    preco: float
    quantidade: int


    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Smartphone",
                "descricao": "Um smartphone avançado",
                "preco": 1999.99,
                "quantidade": 50
            }
        }