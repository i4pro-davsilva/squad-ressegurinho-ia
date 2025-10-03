#!/usr/bin/env python3
"""
Exemplo de uso da conexão com SQL Server
Demonstra como usar a classe SQLServerConnection
"""

from connection_db import SQLServerConnection

def exemplo_uso():
    """Exemplo completo de uso da conexão"""
    
    print("=== Exemplo de Uso - SQL Server Connection ===")
    
    # Criar instância
    db = SQLServerConnection()
    
    try:
        # Conectar
        print("1. Conectando ao servidor...")
        if not db.connect():
            print("❌ Falha na conexão")
            return
        
        print("✅ Conectado com sucesso!")
        
        # Exemplo 1: SELECT @@VERSION
        print("\n2. Executando SELECT @@VERSION...")
        version_result = db.get_version()
        if version_result:
            version = version_result[0][0].split('\n')[0]
            print(f"✅ Versão: {version}")
        
        # Exemplo 2: Consultas de sistema
        print("\n3. Executando consultas de sistema...")
        
        # Listar bancos de dados
        databases = db.execute_query("SELECT name FROM sys.databases WHERE database_id > 4")
        if databases:
            print("✅ Bancos de dados encontrados:")
            for db_name in databases:
                print(f"   - {db_name[0]}")
        
        # Informações do servidor
        server_info = db.execute_query("""
            SELECT 
                SERVERPROPERTY('ServerName') as ServerName,
                SERVERPROPERTY('Edition') as Edition,
                SERVERPROPERTY('ProductVersion') as Version,
                @@SPID as SessionID
        """)
        
        if server_info:
            info = server_info[0]
            print(f"\n✅ Informações do Servidor:")
            print(f"   - Nome: {info[0]}")
            print(f"   - Edição: {info[1]}")
            print(f"   - Versão: {info[2]}")
            print(f"   - Session ID: {info[3]}")
        
        # Exemplo 3: Informações de conexão atual
        connection_info = db.execute_query("""
            SELECT 
                SUSER_NAME() as CurrentUser,
                DB_NAME() as CurrentDatabase,
                @@SERVERNAME as ServerName,
                GETDATE() as CurrentDateTime
        """)
        
        if connection_info:
            conn_info = connection_info[0]
            print(f"\n✅ Informações da Conexão Atual:")
            print(f"   - Usuário: {conn_info[0]}")
            print(f"   - Banco: {conn_info[1]}")
            print(f"   - Servidor: {conn_info[2]}")
            print(f"   - Data/Hora: {conn_info[3]}")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
    
    finally:
        # Sempre fechar a conexão
        print("\n4. Fechando conexão...")
        db.close_connection()
        print("✅ Exemplo concluído!")

if __name__ == "__main__":
    exemplo_uso()