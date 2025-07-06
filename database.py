from typing import Dict, Optional
from models import Produto


class Database:
    def __init__(self):
        self._produtos: Dict[int, Produto] = {}
        self._contador_id = 0

    @property #cria uma interface pública para acessá-lo de forma controlada
    def produtos(self) -> Dict[int, Produto]:
        #Retorna todos os produtos
        return self._produtos

    def gerar_id(self) -> int:
        #Gera um novo ID sequencial
        self._contador_id += 1
        return self._contador_id

    def criar_produto(self, produto: Produto) -> Produto:
        #diciona um novo produto ao banco de dados
        produto.id = self.gerar_id()
        self._produtos[produto.id] = produto
        return produto

    def obter_produto(self, produto_id: int) -> Optional[Produto]:
        #Obtém um produto pelo ID
        return self._produtos.get(produto_id)

    def atualizar_produto(self, produto_id: int, produto: Produto) -> Optional[Produto]:
        #Atualiza um produto existente
        if produto_id not in self._produtos:
            return None

        produto.id = produto_id
        self._produtos[produto_id] = produto
        return produto

    def remover_produto(self, produto_id: int) -> bool:
        """Remove um produto do banco de dados"""
        if produto_id in self._produtos:
            del self._produtos[produto_id]
            return True
        return False

    def listar_produtos(self) -> list[Produto]:  # Alterar o tipo de retorno
        """Lista todos os produtos"""
        return list(self._produtos.values())  # Retorna uma lista dos objetos Produto


# Instância global do banco de dados
db = Database()