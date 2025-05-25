import pyperclip
import nltk
from nltk.chat.util import Chat, reflections

# Baixar os dados do nltk (se necessário)
nltk.download('punkt')

pairs = [
    (r'while\?', ['O comando while executa um bloco de código repetidamente enquanto uma condição é verdadeira.   while(x<=10){x++(codigo onde tudo que estiver aqui ira se repetir 10 vezes)}']),
    (r'for\?', ['O comando for é utilizado para repetir um bloco de código um número específico de vezes, frequentemente usado com uma variável de controle.   for(x=0;x<=10;x++){x++(codigo onde tudo que estiver aqui ira se repetir 10 vezes)}']),
    (r'if\?', ['O comando if é usado para executar um bloco de código apenas se uma condição especificada for verdadeira.   (if x>=y){codigo, se for verdade aqui} else{codigo, se for falso aqui}']),
    (r'case\?', ['O comando switch case permite selecionar um bloco de código para execução com base no valor de uma variável, útil para múltiplas condições.    switch(x){case 1: comando se o valor de x for igual a 1 break; case 2: comando se valor de x for igual a 2 break; default: comando se x for qualquer outro valor break;}']),
    (r'char\?', ['O tipo de dados char armazena um único caractere, como a ou 1, e geralmente ocupa 1 byte    char var = A  (A entre aspas simples)']),
    (r'(.*)', ['Comando não disponível'])
]

chatbot = Chat(pairs, reflections)

def get_ai_response(text):
    try:
        response_text = chatbot.respond(text)
        print(f"Resposta da IA: {response_text}")
        return "[Coragem]" + response_text
    except Exception as e:
        print(f"Erro ao obter resposta da IA: {e}")
        return "[Coragem] Erro ao obter resposta da IA"

def check_clipboard(app):
    current_text = pyperclip.paste()
    print(f"Texto atual da área de transferência: {current_text}")
    if current_text != app.last_text and "[Coragem]" not in current_text:
        app.last_text = current_text
        ai_response = get_ai_response(current_text)
        app.ai_response.set(ai_response)
        pyperclip.copy(ai_response)
        print(f"Resposta copiada para a área de transferência: {ai_response}") 
    app.after(1000, lambda: check_clipboard(app))
