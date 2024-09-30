import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

prompt_sistema = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

llm = genai.GenerativeModel(
  model_name=MODELO_ESCOLHIDO,
  system_instruction=prompt_sistema
)

pergunta = "Liste três produtos de moda sustentável para ir ao shopping."

resposta = llm.generate_content(pergunta)

print(f"A resposta gerada para pergunta é: {resposta.text}")