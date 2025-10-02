# 🤖 Agente Ressegurinho - I4pro

> **Assistente Inteligente para Operações de Resseguro**  
> Automatize e otimize os processos operacionais do módulo de resseguro do sistema ERP I4pro

---

## 📋 **Visão Geral**

O **Agente Ressegurinho** é uma solução de inteligência artificial desenvolvida para revolucionar a operação do módulo de resseguro da I4pro. Através de uma interface de chat moderna e intuitiva, o sistema oferece orientação especializada e automação de tarefas operacionais complexas.

### 🎯 **Problema que Resolve**

- **Complexidade Operacional**: Simplifica processos complexos do sistema de resseguro
- **Curva de Aprendizado**: Reduz o tempo de treinamento de novos operadores
- **Inconsistência de Procedimentos**: Padroniza a execução de tarefas operacionais
- **Acesso à Informação**: Centraliza conhecimento técnico em uma interface acessível
- **Eficiência Operacional**: Automatiza criação de cotações e consultas

---

## 🚀 **Principais Funcionalidades**

### 💬 **Concierge Inteligente**
- **Orientação Passo a Passo**: Guia os usuários através de procedimentos complexos
- **Base de Conhecimento RAG**: Acesso instantâneo a documentação técnica atualizada
- **Respostas Contextuais**: Informações precisas baseadas na documentação oficial I4pro

### 🔧 **Automação de Processos**
- **Criação Automática de Cotações**: Gera cotações através de interface conversacional
- **Consulta de Dados**: Acesso rápido a informações de contratos e exposições
- **Integração API**: Conecta diretamente com o sistema I4pro

### 📊 **Interface Moderna**
- **Chat Responsivo**: Interface web moderna e intuitiva
- **Streaming em Tempo Real**: Respostas imediatas com feedback visual
- **Múltiplas Sessões**: Gerenciamento de conversas e histórico

---

## 🏗️ **Arquitetura da Solução**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Interface     │◄──►│  Agente IA      │◄──►│  Sistema I4pro  │
│   Web (Next.js) │    │  (Python/Agno)  │    │    (APIs)       │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │                 │
                    │ Base de Dados   │         
                    │ PostgreSQL +    │
                    │ Conhecimento    │
                    │                 │
                    └─────────────────┘
```

### 🔍 **Componentes Técnicos**

- **Backend**: Python com framework Agno (AgentOS)
- **Frontend**: Next.js 15 com TypeScript e Tailwind CSS
- **Banco de Dados**: PostgreSQL com extensão pgvector
- **IA**: OpenAI GPT-4 com sistema RAG (Retrieval-Augmented Generation)
- **Containerização**: Docker Compose para ambiente de desenvolvimento

---

## 📈 **Benefícios de Negócio**

### ⚡ **Produtividade**
- **80% menos tempo** na execução de tarefas rotineiras
- **Redução de erros operacionais** através de orientação padronizada
- **Acesso instantâneo** à documentação técnica

### 💰 **Eficiência Operacional**
- **Automação de cotações** reduz tempo de resposta ao cliente
- **Padronização de processos** melhora qualidade do atendimento
- **Redução de dependência** de especialistas para tarefas básicas

### 🎓 **Capacitação**
- **Onboarding acelerado** de novos colaboradores
- **Conhecimento centralizado** e sempre atualizado
- **Redução da curva de aprendizado** do sistema I4pro

---

## 👥 **Casos de Uso**

### 🏢 **Para Operadores de Resseguro**
```
"Como incluir um contrato de resseguro proporcional?"
→ Recebe guia passo a passo personalizado
```

### 📊 **Para Gestores**
```
"Preciso de uma cotação para cliente X com cobertura Y"
→ Sistema gera cotação automaticamente via API
```

### 🎯 **Para Equipe de Suporte**
```
"Como consultar exposição por região?"
→ Orientação detalhada baseada na documentação oficial
```

---

## 🛠️ **Requisitos e Configuração**

### **Pré-requisitos**
- Docker e Docker Compose
- Node.js 18+ (para desenvolvimento frontend)
- Python 3.13+ (para desenvolvimento backend)
- Acesso ao sistema I4pro (APIs)
- Chave API OpenAI

### **Variáveis de Ambiente**
```env
OPENAI_API_KEY=sua_chave_aqui
DATABASE_URL=postgresql://...
I4PRO_API_BASE_URL=https://...
```

---

## 🚦 **Como Executar**

### **Início Rápido**
```bash
# 1. Clone o repositório
git clone [url-do-repositorio]
cd agente_ressegurinho

# 2. Inicie o banco de dados
docker-compose up -d

# 3. Configure as variáveis de ambiente
cp agent/.env.example agent/.env
# Edite o arquivo .env com suas configurações

# 4. Execute o backend
cd agent
python main.py

# 5. Execute o frontend (em outro terminal)
cd agent-ui
npm install
npm run dev
```

### **Acesso**
- **Interface Web**: http://localhost:3000
- **Backend API**: http://localhost:7777
- **Banco de Dados**: localhost:5432

---

## 📚 **Base de Conhecimento**

O sistema utiliza documentação técnica especializada:

- **Documentação de Acúmulo**: Procedimentos de análise de exposição
- **Cadastros**: Configuração de entidades e relacionamentos
- **Contratos**: Gestão completa de contratos de resseguro
- **Borderôs**: Processamento e validação de borderôs
- **Emissões**: Fluxo de emissão de apólices
- **Multilinhas**: Gestão de produtos multi-ramo
- **Offset**: Procedimentos de compensação

---

## 🔒 **Segurança e Compliance**

- **Acesso Controlado**: Integração com sistema de autenticação I4pro
- **Dados Sensíveis**: Criptografia em trânsito e em repouso
- **Auditoria**: Log completo de interações e operações
- **Backup**: Rotinas automatizadas de backup da base de conhecimento

---

## 📞 **Suporte e Contato**

Para dúvidas, sugestões ou suporte técnico:

- **Email**: [email-suporte]
- **Documentação Técnica**: Consulte READMEs específicos em `/agent` e `/agent-ui`
- **Issues**: Utilize o sistema de issues do repositório

---

## 📄 **Licença**

Propriedade da I4pro - Todos os direitos reservados.

---

*Desenvolvido com ❤️ para otimizar as operações de resseguro da I4pro*