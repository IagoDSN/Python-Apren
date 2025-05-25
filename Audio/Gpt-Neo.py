import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import speech_recognition as sr
import pyttsx3

# Inicializar GPT-Neo
model_name = "EleutherAI/gpt-neo-125M" # model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Inicializar reconhecimento de fala
recognizer = sr.Recognizer()

# Inicializar o motor de síntese de fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 1.0)  # Volume da fala

def generate_response(input_text):
    """Gera uma resposta usando GPT-Neo."""
    try:
        # Tokenizar a entrada
        inputs = tokenizer(input_text, return_tensors="pt")

        # Gerar a resposta
        outputs = model.generate(
            inputs["input_ids"],
            max_length=50,  # Limite máximo de tokens na resposta
            temperature=0.7,  # Controla a criatividade
            top_k=50,  # Limita as opções de palavras mais prováveis
            top_p=0.95,  # Torna a geração mais natural
            num_return_sequences=1  # Apenas uma resposta
        )

        # Decodificar a resposta gerada
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

def speak_response(response_text):
    """Converte a resposta em áudio e reproduz."""
    engine.say(response_text)
    engine.runAndWait()

# Reconhecimento de fala e resposta
with sr.Microphone() as source:
    print("Fale algo para que o modelo responda...")

    while True:
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para ruído de fundo
        audio = recognizer.listen(source)  # Captura o áudio
        
        try:
            # Converter áudio para texto
            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            
            # Gerar resposta com GPT-Neo
            response = generate_response(text)
            print("Resposta do modelo: " + response)
            
            # Reproduzir a resposta como áudio
            speak_response(response)
            
            if text.lower() == "sair":
                print("Encerrando o programa...")
                break  # Finaliza o loop
        
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")

print("Programa finalizado.")
