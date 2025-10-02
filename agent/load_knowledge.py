"""
Script para carregar os PDFs na base de conhecimento
Execute este script UMA VEZ para popular o banco de dados
"""

import os
import asyncio
from dotenv import load_dotenv
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.db.postgres.postgres import PostgresDb

# Carregar variáveis de ambiente
load_dotenv()

# Configurar banco de dados
db_url = "postgresql+psycopg://agente_ia:hudweihg78943uihqw$#@localhost:5432/postgres"

db = PostgresDb(
    db_url=db_url,
    knowledge_table="knowledge_contents",
)

# Criar base de conhecimento
knowledge = Knowledge(
    contents_db=db,
    vector_db=PgVector(
        table_name="pdf_knowledge",
        db_url=db_url,
    )
)

# Lista de arquivos para carregar
arquivos = [
    {"path": "base_conhecimento/Doc_Combinado.pdf", "name": "Doc_Combinado", "metadata": {"tipo": "manual", "categoria": "combinado"}},
    {"path": "base_conhecimento/Doc_Contrato_Bordero.pdf", "name": "Doc_Contrato_Bordero", "metadata": {"tipo": "contrato", "categoria": "bordero"}},
    {"path": "base_conhecimento/Doc_Contrato_Emissao.pdf", "name": "Doc_Contrato_Emissao", "metadata": {"tipo": "contrato", "categoria": "emissao"}},
    {"path": "base_conhecimento/Doc_Contrato_Resseguro.pdf", "name": "Doc_Contrato_Resseguro", "metadata": {"tipo": "contrato", "categoria": "resseguro"}},
    {"path": "base_conhecimento/Doc_Multilinhas.pdf", "name": "Doc_Multilinhas", "metadata": {"tipo": "manual", "categoria": "multilinhas"}},
    {"path": "base_conhecimento/Doc_Offset.pdf", "name": "Doc_Offset", "metadata": {"tipo": "manual", "categoria": "offset"}},
    {"path": "base_conhecimento/Documentacao_Acumulo.pdf", "name": "Documentacao_Acumulo", "metadata": {"tipo": "documentacao", "categoria": "acumulo"}},
    {"path": "base_conhecimento/Documentacao_Cadastros.pdf", "name": "Documentacao_Cadastros", "metadata": {"tipo": "documentacao", "categoria": "cadastros"}},
]

async def load_all_pdfs():
    """Carrega todos os PDFs na base de conhecimento"""
    print("🚀 Iniciando carregamento dos PDFs...")
    print(f"📊 Total de arquivos: {len(arquivos)}\n")
    
    for i, arquivo in enumerate(arquivos, 1):
        print(f"📄 [{i}/{len(arquivos)}] Carregando: {arquivo['name']}...")
        try:
            await knowledge.add_content_async(
                path=arquivo["path"],
                name=arquivo["name"],
                metadata=arquivo["metadata"]
            )
            print(f"✅ {arquivo['name']} carregado com sucesso!\n")
        except Exception as e:
            print(f"❌ Erro ao carregar {arquivo['name']}: {e}\n")
    
    print("🎉 Carregamento concluído!")
    print("💡 Agora você pode executar: uv run main.py")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERRO: Configure a variável OPENAI_API_KEY no arquivo .env")
        exit(1)
    
    asyncio.run(load_all_pdfs())

