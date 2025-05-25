from transformers import AutoModelForCausalLM, AutoTokenizer

# Carregar modelo GPT-J
model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Função para gerar resposta
def gerar_texto(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=200, temperature=0.9)
    return tokenizer.decode(output[0], skip_special_tokens=True)
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Tchau! Até a próxima!")
        break
    print("GPT-J:", gerar_texto(user_input))
