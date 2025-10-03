import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connection_db import SQLServerConnection
from typing import List, Dict, Optional

def consulta_produto(cd_produto: Optional[int] = None, nm_produto: Optional[str] = None) -> str:
    """Consulta produtos na base de dados corp_produto.
    
    Esta função conecta ao banco de dados e retorna informações sobre produtos
    para auxiliar o agente na criação de cotações e massas de dados.
    
    Args:
        cd_produto: Código específico do produto para buscar (opcional)
        nm_produto: Nome ou parte do nome do produto para buscar (opcional)
    
    Returns:
        str: Lista formatada dos produtos encontrados com cd_produto e nm_produto
    """
    
    db = SQLServerConnection()
    
    try:
        # Conecta ao banco de dados reag_erp_head
        if not db.connect(database="reag_erp_head"):
            return "Erro: Não foi possível conectar ao banco de dados reag_erp_head."
        
        # Monta a query baseada nos parâmetros
        if cd_produto is not None:
            query = f"""
            SELECT cd_produto, nm_produto 
            FROM corp_produto 
            WHERE cd_produto = {cd_produto}
            ORDER BY nm_produto
            """
        elif nm_produto is not None:
            query = f"""
            SELECT cd_produto, nm_produto 
            FROM corp_produto 
            WHERE nm_produto LIKE '%{nm_produto}%'
            ORDER BY nm_produto
            """
        else:
            # Se nenhum parâmetro foi fornecido, retorna todos os produtos
            query = """
            SELECT cd_produto, nm_produto 
            FROM corp_produto 
            ORDER BY nm_produto
            """
        
        # Executa a query
        results = db.execute_query(query)
        
        if not results:
            return "Nenhum produto encontrado com os critérios especificados."
        
        # Formata os resultados
        produtos_list = []
        for row in results:
            cd_produto_result = row[0]
            nm_produto_result = row[1]
            produtos_list.append(f"Código: {cd_produto_result} - Nome: {nm_produto_result}")
        
        # Monta a resposta formatada
        header = f"=== PRODUTOS ENCONTRADOS ({len(produtos_list)}) ==="
        produtos_formatados = "\n".join(produtos_list)
        
        return f"{header}\n{produtos_formatados}"
        
    except Exception as e:
        return f"Erro ao consultar produtos: {str(e)}"
    
    finally:
        # Sempre fecha a conexão
        db.close_connection()


def listar_todos_produtos() -> str:
    """Função de conveniência para listar todos os produtos disponíveis."""
    return consulta_produto()


def buscar_produto_por_codigo(cd_produto: int) -> str:
    """Função de conveniência para buscar produto por código específico."""
    return consulta_produto(cd_produto=cd_produto)


def buscar_produto_por_nome(nm_produto: str) -> str:
    """Função de conveniência para buscar produtos por nome ou parte do nome."""
    return consulta_produto(nm_produto=nm_produto)


if __name__ == "__main__":
    # Testes da função
    print("=== TESTANDO CONSULTA DE PRODUTOS ===")
    print("\n1. Listando todos os produtos:")
    resultado = listar_todos_produtos()
    print(resultado)
    
    print("\n2. Buscando produto por código (exemplo - código 1):")
    resultado = buscar_produto_por_codigo(1)
    print(resultado)
    
    print("\n3. Buscando produtos por nome (exemplo - 'seguro'):")
    resultado = buscar_produto_por_nome("seguro")
    print(resultado)