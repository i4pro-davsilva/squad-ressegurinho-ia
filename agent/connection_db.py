import pymssql
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from typing import Optional

class SQLServerConnection:
    """Classe para gerenciar conexão com SQL Server usando pymssql"""
    
    def __init__(self):
        self.server = "wolverine"
        self.username = "ggomes.poc"
        self.password = "4Ey8nfZsqGDTJT2}ZA31TJRO93AYAz"
        self.database = "master"  # Banco padrão
        self.engine = None
        self.session = None
    
    def create_connection_string(self, database: Optional[str] = None) -> str:
        """Cria a string de conexão para SQL Server usando pymssql"""
        db = database or self.database
        
        # String de conexão usando pymssql
        connection_string = (
            f"mssql+pymssql://{self.username}:{self.password}@{self.server}/{db}"
        )
        
        return connection_string
    
    def connect(self, database: Optional[str] = None):
        """Estabelece conexão com o banco de dados"""
        try:
            connection_string = self.create_connection_string(database)
            self.engine = create_engine(connection_string, echo=True)
            
            # Testa a conexão
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT @@VERSION"))
                version = result.fetchone()[0]
                print(f"Conexão estabelecida com sucesso!")
                print(f"Versão do SQL Server: {version[:100]}...")
            
            # Cria session factory
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            
            return True
            
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
    
    def execute_query(self, query: str):
        """Executa uma query SQL"""
        try:
            if not self.engine:
                print("Conexão não estabelecida. Chame connect() primeiro.")
                return None
            
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                
                # Se for uma query SELECT, retorna os resultados
                if query.strip().upper().startswith('SELECT'):
                    return result.fetchall()
                else:
                    conn.commit()
                    return result.rowcount
                    
        except Exception as e:
            print(f"Erro ao executar query: {e}")
            return None
    
    def get_version(self):
        """Retorna a versão do SQL Server"""
        return self.execute_query("SELECT @@VERSION")
    
    def close_connection(self):
        """Fecha a conexão com o banco de dados"""
        try:
            if self.session:
                self.session.close()
            if self.engine:
                self.engine.dispose()
            print("Conexão fechada com sucesso!")
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")

# Função de conveniência para uso rápido
def test_connection():
    """Testa a conexão e executa SELECT @@VERSION"""
    db = SQLServerConnection()
    
    if db.connect():
        print("\n=== Testando SELECT @@VERSION ===")
        version = db.get_version()
        if version:
            print(f"Versão completa: {version[0][0]}")
        
        db.close_connection()
        return True
    else:
        return False

if __name__ == "__main__":
    # Teste da conexão
    test_connection()