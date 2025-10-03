import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.knowledge.knowledge import Knowledge
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector
from agno.db.postgres.postgres import PostgresDb
import asyncio
from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI
from tools.criar_cotacao import criar_cotacao
from tools.consulta_produto import consulta_produto, buscar_produto_por_nome
from tools.buscar_codigo_produto import buscar_codigo_produto
from config.agent_instructions import (
    AGENT_CONCIERGE_INSTRUCTIONS,
    AGENT_CRIADOR_MASSAS_INSTRUCTIONS
)

# Carregar variáveis de ambiente
load_dotenv()

# Validar variáveis de ambiente obrigatórias
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY não configurada no arquivo .env")

# db_url = os.getenv("DATABASE_URL")
# if not db_url:
#     raise ValueError("DATABASE_URL não configurada no arquivo .env")

# db = PostgresDb(
#     db_url=db_url,
#     knowledge_table="knowledge_contents",
# )

# # Criar base de conhecimento
# knowledge = Knowledge(
#     contents_db=db,
#     vector_db=PgVector(
#         table_name="pdf_knowledge",
#         db_url=db_url,
#     )
# )


model = OpenAIChat(
    id="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)

### BLOCO DE AGENTES ###
agent_rag = Agent(
    name="Concierge Modulo Resseguro I4pro",
    search_knowledge=True,
    system_message="Você é o Concierge do Módulo de Resseguro da I4pro — um assistente especializado que orienta os usuários PASSO A PASSO na execução de tarefas operacionais dentro do sistema ERP da I4pro.",
    db=SqliteDb(db_file="tmp/agents.db"),
    markdown=True,
    add_history_to_context=True,
    model=model,
    instructions=AGENT_CONCIERGE_INSTRUCTIONS,
    debug_mode=True,
)

# ====================== TOOLS AGENTE MASSA DE DADOS ====================== #

tools = [
    criar_cotacao,
    consulta_produto,
    buscar_produto_por_nome,
    buscar_codigo_produto,
]

agent_criador_massas = Agent(
    name="Criador de Massas",
    db=SqliteDb(db_file="tmp/agents.db"),
    markdown=True,
    add_history_to_context=True,
    model=model,
    instructions=AGENT_CRIADOR_MASSAS_INSTRUCTIONS,
    debug_mode=True,
    tools=tools
)



# Configurar AgentOS
agent_os = AgentOS(
    agents=[agent_rag, agent_criador_massas],
    interfaces=[AGUI(agent=agent_rag), AGUI(agent=agent_criador_massas)]
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)


