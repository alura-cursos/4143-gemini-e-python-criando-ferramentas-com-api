import google.generativeai as genai

MODELO_FLASH = "gemini-1.5-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limites_modelo_flash = {
  "tokens_entrada" : model_flash.input_token_limit,
  "tokens_saida" : model_flash.output_token_limit
}

print(f"Limites do modelo flash são: {limites_modelo_flash}")

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limites_modelo_pro = {
  "tokens_entrada" : model_pro.input_token_limit,
  "tokens_saida" : model_pro.output_token_limit
}

print(f"Limites do modelo pro são: {limites_modelo_pro}")

llm_flash = genai.GenerativeModel(
  f"models/{MODELO_FLASH}"
)

quantidade_tokens = llm_flash.count_tokens("O que é uma calça de shopping?")
print(f"A quantidade de tokens é: {quantidade_tokens}")

resposta = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_resposta * CUSTO_SAIDA_FLASH) / 1000000
print("Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_resposta * CUSTO_SAIDA_PRO) / 1000000
print("Custo Total U$ Pro: ", custo_total)

# 0.0000663 flash
# 0.0023309 pro