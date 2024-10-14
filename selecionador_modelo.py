import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GEMINI)
modelo = "gemini-1.5-flash"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("dados\lista_de_compras_100_clientes.csv")

modelo_flash  = genai.GenerativeModel(f"models/{modelo}")
qtd_tokens = modelo_flash.count_tokens(prompt_usuario)

LIMITE_TOKENS  = 3000

if qtd_tokens.total_tokens >= LIMITE_TOKENS:
    modelo = "gemini-1.5-pro"

print(f"O modelo selecionado foi: {modelo}")

llm = genai.GenerativeModel(
    model_name=modelo,
    system_instruction=prompt_sistema
)

resposta = llm.generate_content(prompt_usuario)
print(f"Resposta: {resposta.text}")