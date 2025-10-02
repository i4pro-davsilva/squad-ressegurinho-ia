import httpx
from typing import List, Dict, Optional
from datetime import datetime

def criar_cotacao(
    cd_produto: int,
    cd_filial: int,
    id_pessoa_cliente: int,
    id_endereco_cliente: int,
    id_pessoa_tomador: int,
    id_endereco_tomador: int,
    dt_inicio_vigencia: str,
    dt_fim_vigencia: str,
    corretores: List[Dict],
    coberturas: List[Dict] = None,
    cd_tp_resseguro: int = None,
    id_produto_parc_premio: int = None,
    cd_forma_pagamento: int = None,
    dt_vencimento_pparcela: str = None,
    nm_texto: str = None,
    nm_texto_anexo: str = None
) -> str:
    """Cria uma cotação no sistema através da API.
    
    Args:
        cd_produto: Código do produto (obrigatório)
        cd_filial: Código da filial (obrigatório)
        id_pessoa_cliente: ID da pessoa cliente (obrigatório)
        id_endereco_cliente: ID do endereço cliente (obrigatório)
        id_pessoa_tomador: ID da pessoa tomador (obrigatório)
        id_endereco_tomador: ID do endereço tomador (obrigatório)
        dt_inicio_vigencia: Data início vigência (ISO8601: yyyy-mm-ddThh:mm:ss)
        dt_fim_vigencia: Data fim vigência (ISO8601: yyyy-mm-ddThh:mm:ss)
        corretores: Lista de corretores [{"id_pessoa_corretor": int, "cd_tp_comissao": int, "pe_comissao": float, "dv_lider": bool}]
        coberturas: Lista de coberturas (opcional)
        cd_tp_resseguro: Código tipo resseguro (opcional)
        id_produto_parc_premio: ID produto parcela prêmio (opcional)
        cd_forma_pagamento: Código forma pagamento (opcional)
        dt_vencimento_pparcela: Data vencimento primeira parcela (opcional)
        nm_texto: Texto (opcional)
        nm_texto_anexo: Texto anexo (opcional)
    
    Returns:
        str: Resposta da API
    """
    
    # Montar payload
    payload = {
        "cd_produto": cd_produto,
        "cd_filial": cd_filial,
        "id_pessoa_cliente": id_pessoa_cliente,
        "id_endereco_cliente": id_endereco_cliente,
        "id_pessoa_tomador": id_pessoa_tomador,
        "id_endereco_tomador": id_endereco_tomador,
        "dt_inicio_vigencia": dt_inicio_vigencia,
        "dt_fim_vigencia": dt_fim_vigencia,
        "InserirCotacaoCorretor": corretores
    }
    
    # Adicionar campos opcionais se fornecidos
    if cd_tp_resseguro is not None:
        payload["cd_tp_resseguro"] = cd_tp_resseguro
    if id_produto_parc_premio is not None:
        payload["id_produto_parc_premio"] = id_produto_parc_premio
    if cd_forma_pagamento is not None:
        payload["cd_forma_pagamento"] = cd_forma_pagamento
    if dt_vencimento_pparcela is not None:
        payload["dt_vencimento_pparcela"] = dt_vencimento_pparcela
    if nm_texto is not None:
        payload["nm_texto"] = nm_texto
    if nm_texto_anexo is not None:
        payload["nm_texto_anexo"] = nm_texto_anexo
    if coberturas is not None:
        payload["InserirCotacaoCobertura"] = coberturas
    
    try:
        response = httpx.post(
            "http://sitehead03/reag/erpws/run/API_GAR_v1/InserirCotacao",
            json=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            timeout=30
        )
        
        return f"Status: {response.status_code}\nResposta: {response.text}"
        
    except Exception as e:
        return f"Erro ao criar cotação: {str(e)}"
