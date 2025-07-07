import openai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Carrega chave da OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extrair_texto_pdf(caminho_arquivo):
    reader = PdfReader(caminho_arquivo)
    texto = ""
    for pagina in reader.pages:
        texto += pagina.extract_text() or ""
    return texto

def analyze_document_with_esg_guidelines(file_path: str, pergunta: str) -> dict:
    caminho_completo = os.path.join("app", "uploads", file_path)
    texto_documento = extrair_texto_pdf(caminho_completo)

    prompt = f"""
Você é um assistente que avalia a conformidade de documentos com diretrizes ESG (ambientais, sociais e de governança).
Analise o conteúdo a seguir e responda à pergunta do usuário com base nesse documento:

--- DOCUMENTO ESG ---
{texto_documento[:3000]}
--- FIM DO DOCUMENTO ---

Pergunta: {pergunta}
Resposta:"""

    resposta = openai.ChatCompletion.create(
        model="gpt-4",  # ou "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )

    resposta_final = resposta["choices"][0]["message"]["content"].strip()

    return {
        "pergunta": pergunta,
        "resposta": f"""
            <strong>Pergunta:</strong> {pergunta}<br>
            <strong>Arquivo analisado:</strong> {file_path}<br><br>
            <strong>Resultado:</strong><br>{resposta_final}
        """
    }

