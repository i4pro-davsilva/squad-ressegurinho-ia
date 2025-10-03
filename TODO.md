# 📝 TODO - Agente Ressegurinho

> Lista de tarefas pendentes para finalização do ecossistema de agentes de resseguro

---

## 🚧 **Pendências Críticas**

### 1. **Revisar os Prompts dos Agentes** 
- [ ] Revisar prompt do agente principal (`agent/config/agent_instructions.py`)
- [ ] Otimizar contexto para operações de resseguro
- [ ] Validar terminologia técnica específica da I4Pro
- [ ] Ajustar tom de voz e personalidade do agente
- [ ] Testar cenários de erro e casos extremos

### 2. **Estabelecer o Flow de Conversa do Agente Criador de Cotações**
- [ ] **Fluxo estruturado de perguntas**:
  - [ ] 2.1. Pergunta sobre o produto desejado
  - [ ] 2.2. Pergunta sobre cobertura necessária
  - [ ] 2.3. Pergunta sobre valores de exposição
  - [ ] 2.4. Pergunta sobre período de vigência
  - [ ] 2.5. Pergunta sobre localização/região
  - [ ] 2.6. Confirmação dos dados antes de criar cotação
- [ ] Implementar validação de dados em cada etapa
- [ ] Criar sistema de retry para informações inválidas
- [ ] Adicionar funcionalidade de "voltar etapa anterior"

### 3. **Conectar com o Banco de Dados**
- [ ] Configurar conexão com BD I4Pro
- [ ] Testar conectividade e performance
- [ ] Implementar pool de conexões
- [ ] Configurar variáveis de ambiente para credenciais

### 3.1. **Tools de Consulta ao Banco de Dados**
- [ ] **Tool: Consultar Produtos**
  - [ ] Query para obter nomes dos produtos
  - [ ] Query para obter cd_produto correspondente
  - [ ] Implementar cache para consultas frequentes
- [ ] **Tool: Consultar Coberturas**
  - [ ] Query para coberturas por produto
  - [ ] Query para cd_cobertura correspondente
- [ ] **Tool: Consultar Apólices/Contratos**
  - [ ] Query para contratos ativos
  - [ ] Query para histórico de contratos

---

## 🔧 **Melhorias Técnicas**

### 5. **Base de Conhecimento RAG**
- [ ] Atualizar documentos na pasta `base_conhecimento/`
- [ ] Implementar versionamento de documentos
- [ ] Otimizar chunks e embeddings
- [ ] Adicionar métricas de relevância das respostas
- [ ] Implementar reindexação automática

### 6. **Ferramentas (Tools)**
- [ ] Expandir `criar_cotacao.py` com validações robustas
- [ ] Criar tool para consultar histórico de cotações
- [ ] Implementar tool para gerar relatórios
- [ ] Criar tool para validação de dados regulatórios
- [ ] Implementar tool para cálculo de comissões


## 📚 **Documentação**

### 13. **Documentação Técnica**
- [ ] Documentar arquitetura da solução
- [ ] Criar guia de deploy e configuração
- [ ] Documentar APIs e tools disponíveis
- [ ] Criar troubleshooting guide
- [ ] Documentar processo de atualização

### 14. **Documentação do Usuário**
- [ ] Manual do usuário final
- [ ] Guia de primeiros passos
- [ ] FAQ com casos comuns
- [ ] Vídeos tutoriais
- [ ] Glossário de termos técnicos

---

## 🎯 **Próximos Passos Imediatos**

**Prioridade Alta:**
1. ✅ Conectar com banco de dados I4Pro
2. ✅ Implementar tool de consulta de produtos
3. ✅ Revisar e otimizar prompts principais
4. ✅ Estruturar fluxo de criação de cotações

**Prioridade Média:**
5. ✅ Melhorar interface de usuário
6. ✅ Implementar logs e monitoramento básico
7. ✅ Criar testes automatizados básicos

**Prioridade Baixa:**
8. ✅ Funcionalidades avançadas
9. ✅ Integrações externas
10. ✅ Documentação completa

---

## 📝 **Notas**

- **Ambiente de desenvolvimento**: Usar Docker Compose para facilitar setup
- **Banco de dados**: PostgreSQL com pgvector para RAG
- **LLM**: Configurado para usar múltiplos provedores (Claude, GPT, etc.)
- **Deploy**: Preparar para ambiente Kubernetes/Docker

---

**Última atualização**: 02/10/2025  
**Responsável**: Squad Ressegurinho IA  
**Status**: Em desenvolvimento ativo 🚀