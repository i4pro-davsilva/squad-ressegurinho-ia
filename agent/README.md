# Sistema Multi-Agente Resseguro I4pro 🤖

Sistema inteligente com múltiplos agentes especializados para o módulo de Resseguro do ERP I4pro, construído com o framework Agno.

## 🚀 Funcionalidades

- **2 Agentes Especializados**: Concierge e Criador de Massas
- **Base de Conhecimento RAG**: 8 PDFs técnicos + PostgreSQL com pgvector
- **AgentOS + AGUI**: Interface moderna multi-agente
- **Ferramentas Customizadas**: API de criação de cotações
- **Busca Semântica Avançada**: Respostas baseadas em documentação real

## 📋 Pré-requisitos

- Python 3.13+
- Docker e Docker Compose
- Chave da API OpenAI
- uv (gerenciador de pacotes)

## 🛠️ Instalação

### 1. Inicie o PostgreSQL com pgvector
```bash
cd ..  # Voltar para raiz do projeto
docker-compose up -d
```

### 2. Navegue para a pasta agent e instale dependências
```bash
cd agent
uv sync
```

### 3. Configure a API Key
Crie um arquivo `.env` na pasta `agent/`:
```bash
OPENAI_API_KEY=sua_chave_openai_aqui
```

## 🎮 Como Usar

### Passo 1: Carregar os PDFs (Execute apenas UMA VEZ)
```bash
uv run load_knowledge.py
```

Este comando vai:
- Ler todos os PDFs da pasta `base_conhecimento/`
- Gerar embeddings usando OpenAI
- Armazenar no PostgreSQL com pgvector

⏱️ **Tempo estimado:** 5-10 minutos (depende do tamanho dos PDFs e da API da OpenAI)

### Passo 2: Iniciar o Agente
```bash
uv run main.py
```

Acesse a interface AGUI em: **http://localhost:8000**

## 🤖 Agentes Disponíveis

### 1. **Concierge Módulo Resseguro I4pro** 🎯
**Função:** Orientar usuários passo a passo nas tarefas operacionais do sistema

**Características:**
- Busca exclusiva na base de conhecimento
- Respostas diretas e objetivas
- Guia operacional com passos numerados
- Cita sempre o documento-fonte
- Não inventa informações fora da base

**Exemplos de uso:**
- "Como incluir um contrato de resseguro?"
- "Como gerar um bordereau?"
- "Como consultar exposição acumulada?"
- "Quais os campos obrigatórios para cadastro de contrato?"

### 2. **Criador de Massas de Teste** 🔧
**Função:** Criar dados de teste para o módulo de resseguro

**Características:**
- Coleta informações em blocos sequenciais
- Valida campos obrigatórios vs opcionais
- Integração com API de cotações
- Formato de dados padronizado (ISO8601, decimal inglês)

**Ferramentas disponíveis:**
- `criar_cotacao`: Cria cotação completa via API

**Fluxo de trabalho:**
1. Coleta informações da cotação (produto, filial, cliente, datas)
2. Coleta dados do corretor (ID, comissão, tipo)
3. Coleta informações de cobertura (IS, taxa, prêmio)
4. Cria a cotação via API

## 🏗️ Estrutura do Projeto

```
agent/
├── main.py                    # Configuração dos agentes e AgentOS
├── load_knowledge.py          # Script para carregar PDFs na base
├── tools/
│   └── criar_cotacao.py      # Ferramenta para criar cotações via API
├── base_conhecimento/        # PDFs de documentação (8 arquivos)
│   ├── Doc_Combinado.pdf
│   ├── Doc_Contrato_Bordero.pdf
│   ├── Doc_Contrato_Emissao.pdf
│   ├── Doc_Contrato_Resseguro.pdf
│   ├── Doc_Multilinhas.pdf
│   ├── Doc_Offset.pdf
│   ├── Documentacao_Acumulo.pdf
│   └── Documentacao_Cadastros.pdf
├── pyproject.toml            # Dependências do projeto
└── .env                      # Variáveis de ambiente (não versionado)
```

## 📚 Base de Conhecimento

### Documentos Técnicos (pasta base_conhecimento/)
- **Doc_Combinado.pdf**: Documentação consolidada do módulo
- **Doc_Contrato_Bordero.pdf**: Processos de borderô e contratos
- **Doc_Contrato_Emissao.pdf**: Fluxo de emissão de contratos
- **Doc_Contrato_Resseguro.pdf**: Gestão de contratos de resseguro
- **Doc_Multilinhas.pdf**: Operações com contratos multilinhas
- **Doc_Offset.pdf**: Processos de offset
- **Documentacao_Acumulo.pdf**: Controle de acúmulo e exposição
- **Documentacao_Cadastros.pdf**: Cadastros e parametrizações

## 🔧 Personalização

### Adicionar Novos PDFs à Base
1. Coloque os PDFs na pasta `base_conhecimento/`
2. Edite `load_knowledge.py` e adicione o novo arquivo:
```python
arquivos = [
    # ... PDFs existentes ...
    {"path": "base_conhecimento/Novo_Documento.pdf", "name": "Novo_Documento", "metadata": {"tipo": "manual"}},
]
```
3. Execute: `uv run load_knowledge.py`

### Criar Novas Ferramentas (Tools)
Crie um arquivo em `tools/` seguindo o padrão:
```python
def minha_ferramenta(parametro: str) -> str:
    """Descrição da ferramenta que o agente verá"""
    # Sua lógica aqui
    return "resultado"
```

Depois adicione ao agente em `main.py`:
```python
from tools.minha_ferramenta import minha_ferramenta

tools = [criar_cotacao, minha_ferramenta]
```

### Modificar Comportamento dos Agentes
Edite `system_message` e `instructions` no `main.py`:
```python
agent = Agent(
    name="Meu Agente",
    system_message="Você é um...",
    instructions=[
        "Regra 1...",
        "Regra 2...",
    ],
)
```

## 💡 Exemplos de Uso

### Para o Concierge:
```
👤 Usuário: "Como incluir um novo contrato de resseguro no sistema?"

🤖 Concierge: 
1. Acesse o menu Resseguros > Contratos
2. Clique em "Novo Contrato"
3. Informe o código do produto...
[continua com passos detalhados]

Fonte: Doc_Contrato_Resseguro.pdf
```

### Para o Criador de Massas:
```
👤 Usuário: "Preciso criar uma cotação de teste"

🤖 Criador: 
Vou coletar as informações necessárias em blocos.

**Bloco 1 - Informações da Cotação:**
- Qual o código do produto (cd_produto)?
- Qual o código da filial (cd_filial)?
[continua coletando dados...]
```

## 🐛 Troubleshooting

### ❌ Erro: "OPENAI_API_KEY não configurada"
**Solução:**
1. Crie o arquivo `.env` na pasta `agent/`
2. Adicione: `OPENAI_API_KEY=sk-...`

### ❌ Erro: "extension vector is not available"
**Solução:**
```bash
cd ..
docker-compose down
docker-compose up -d
```
Certifique-se que está usando a imagem `pgvector/pgvector:pg15`

### ❌ Erro: "expected 1536 dimensions, not 0"
**Causa:** Embeddings vazios (API key inválida ou sem saldo)
**Solução:** Verifique sua chave OpenAI e saldo da conta

### ❌ Erro: "RuntimeError: asyncio.run() cannot be called from a running event loop"
**Solução:** Use `load_knowledge.py` separadamente, ANTES de executar `main.py`

### 🔄 Recarregar Base de Conhecimento
Para reprocessar os PDFs:
```bash
# Método 1: Limpar e recarregar
docker-compose down -v
docker-compose up -d
uv run load_knowledge.py

# Método 2: Apenas reexecutar
uv run load_knowledge.py
```

## 🔗 Links Úteis

### Documentação Agno
- [Documentação Oficial](https://docs.agno.ai)
- [Agents Guide](https://docs.agno.ai/agents/introduction)
- [Knowledge Base](https://docs.agno.ai/knowledge/introduction)
- [Tools](https://docs.agno.ai/tools/introduction)
- [AgentOS](https://docs.agno.ai/agent-os/introduction)

### APIs I4pro
- Documentação da API (interna)
- Swagger/OpenAPI endpoint

## 🚀 Roadmap

### Em Desenvolvimento
- [ ] Mais agentes especializados (Sinistros, Apólices, Relatórios)
- [ ] Ferramentas de integração com I4pro (CRUD completo)
- [ ] Dashboard de métricas de uso dos agentes
- [ ] Cache de respostas frequentes

### Planejado
- [ ] Agent de validação de dados
- [ ] Workflows automatizados para processos complexos
- [ ] Integração com sistemas externos (seguradoras, resseguradoras)
- [ ] Análise de documentos e extração de dados

## 📊 Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                        AGUI Interface                        │
│                     (http://localhost:8000)                  │
└────────────────────┬───────────────────┬────────────────────┘
                     │                   │
         ┌───────────▼──────────┐   ┌───▼────────────────┐
         │  Concierge Agent     │   │  Criador Massas    │
         │  - RAG Knowledge     │   │  - Tools API       │
         │  - Search Semantic   │   │  - Validation      │
         └───────────┬──────────┘   └───┬────────────────┘
                     │                   │
         ┌───────────▼───────────────────▼────────────────┐
         │          PostgreSQL + pgvector                  │
         │  - Vector embeddings (1536 dimensions)          │
         │  - Knowledge contents                           │
         │  - Agent history & state                        │
         └─────────────────────────────────────────────────┘
```

## 👥 Contribuindo

Para adicionar novos agentes ou ferramentas:

1. Crie a ferramenta em `tools/`
2. Configure o agente em `main.py`
3. Adicione à lista de agentes do AgentOS
4. Documente no README
5. Teste com casos reais

## 📝 Licença

Projeto interno I4pro - Todos os direitos reservados
