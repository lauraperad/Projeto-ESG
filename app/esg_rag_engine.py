def analyze_document_with_esg_guidelines(file_path: str, pergunta: str) -> dict:
    resposta_simulada = f"""
    <strong>Pergunta:</strong> {pergunta}<br>
    <strong>Arquivo analisado:</strong> {file_path}<br><br>
    <strong>Resultado:</strong> Documento parcialmente compatível com diretrizes ESG.<br>
    Recomenda-se reforçar práticas de gestão ambiental e governança.
    """
    return {
        "pergunta": pergunta,
        "resposta": resposta_simulada
    }
