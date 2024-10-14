import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

prompt_sistema = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

configuracao_modelo = {
  "temperature" : 0.1,
  "top_p" : 1.0,
  "top_k" : 2,
  "max_output_tokens" : 8192,
  "response_mime_type" : "text/plain"
}

llm = genai.GenerativeModel(
  model_name=MODELO_ESCOLHIDO,
  system_instruction=prompt_sistema,
  generation_config=configuracao_modelo
)

pergunta = "Liste três produtos de moda sustentável para ir ao shopping."

resposta = llm.generate_content(pergunta)

print(f"A resposta gerada para pergunta é: {resposta.text}")