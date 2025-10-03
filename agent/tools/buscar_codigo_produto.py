import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connection_db import SQLServerConnection
from typing import Optional

def obter_codigo_produto_por_nome(nm_produto: str) -> Optional[int]:
    """Busca o código de um produto pelo nome exato ou parte do nome.
    
    Esta função é otimizada para o agente criador de massas converter
    nomes de produtos informados pelo usuário em códigos para usar na API.
    
    Args:
        nm_produto: Nome do produto ou parte do nome
    
    Returns:
        int: Código do produto se encontrado, None se não encontrado ou múltiplos encontrados
    """
    
    db = SQLServerConnection()
    
    try:
        # Conecta ao banco de dados reag_erp_head
        if not db.connect(database="reag_erp_head"):
            return None
        
        # Primeiro tenta busca exata
        query_exata = f"""
        SELECT cd_produto, nm_produto 
        FROM corp_produto 
        WHERE nm_produto = '{nm_produto}'
        """
        
        results = db.execute_query(query_exata)
        
        if results and len(results) == 1:
            return results[0][0]  # Retorna o cd_produto
        
        # Se não encontrou exato, tenta busca parcial
        query_parcial = f"""
        SELECT cd_produto, nm_produto 
        FROM corp_produto 
        WHERE nm_produto LIKE '%{nm_produto}%'
        ORDER BY nm_produto
        """
        
        results = db.execute_query(query_parcial)
        
        if results:
            if len(results) == 1:
                return results[0][0]  # Retorna o único resultado
            else:
                # Múltiplos resultados - retorna None para o agente pedir especificação
                return None
        
        return None  # Nenhum resultado encontrado
        
    except Exception as e:
        return None
    
    finally:
        # Sempre fecha a conexão
        db.close_connection()


def buscar_codigo_produto(nm_produto: str) -> str:
    """Função wrapper para uso do agente - retorna resposta formatada.
    
    Args:
        nm_produto: Nome do produto para buscar
    
    Returns:
        str: Mensagem formatada com o resultado da busca
    """
    
    if not nm_produto or not nm_produto.strip():
        return "❌ Nome do produto não pode estar vazio."
    
    db = SQLServerConnection()
    
    try:
        # Conecta ao banco de dados reag_erp_head
        if not db.connect(database="reag_erp_head"):
            return "❌ Erro ao conectar ao banco de dados."
        
        # Primeiro tenta busca exata
        query_exata = f"""
        SELECT cd_produto, nm_produto 
        FROM corp_produto 
        WHERE nm_produto = '{nm_produto.strip()}'
        """
        
        results = db.execute_query(query_exata)
        
        if results and len(results) == 1:
            codigo = results[0][0]
            nome = results[0][1]
            return f"✅ Produto encontrado: {codigo} - {nome}"
        
        # Se não encontrou exato, tenta busca parcial
        query_parcial = f"""
        SELECT cd_produto, nm_produto 
        FROM corp_produto 
        WHERE nm_produto LIKE '%{nm_produto.strip()}%'
        ORDER BY nm_produto
        """
        
        results = db.execute_query(query_parcial)
        
        if results:
            if len(results) == 1:
                codigo = results[0][0]
                nome = results[0][1]
                return f"✅ Produto encontrado: {codigo} - {nome}"
            else:
                # Múltiplos resultados
                produtos_list = []
                for row in results:
                    produtos_list.append(f"Código: {row[0]} - Nome: {row[1]}")
                
                produtos_formatados = "\n".join(produtos_list)
                return f"❌ Nome '{nm_produto}' corresponde a múltiplos produtos. Seja mais específico:\n\n{produtos_formatados}"
        
        return f"❌ Nenhum produto encontrado com o nome '{nm_produto}'.\n💡 Use a função 'consulta_produto' para ver todos os produtos disponíveis."
        
    except Exception as e:
        return f"❌ Erro ao buscar produto: {str(e)}"
    
    finally:
        # Sempre fecha a conexão
        db.close_connection()


if __name__ == "__main__":
    # Testes da função
    print("=== TESTANDO BUSCA DE CÓDIGO POR NOME ===")
    
    print("\n1. Testando nome exato:")
    resultado = buscar_codigo_produto("Residencial")
    print(resultado)
    
    print("\n2. Testando busca parcial:")
    resultado = buscar_codigo_produto("GARANTIA")
    print(resultado)
    
    print("\n3. Testando nome não encontrado:")
    resultado = buscar_codigo_produto("Produto Inexistente")
    print(resultado)