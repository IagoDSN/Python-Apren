import subprocess

def chat_with_ollama(message):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=message.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

while True:
    user_input = input("Você: ")
    if user_input.lower() in ['sair', 'exit', 'quit']:
        break
    resposta = chat_with_ollama(user_input)
    print("Bot:", resposta)

# ollama run mistral
 