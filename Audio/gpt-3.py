import openai
import speech_recognition as sr
import pyttsx3

# Configure sua chave de API da OpenAI
openai.api_key = "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"  # Substitua pela sua chave da OpenAI

# Inicializar reconhecimento de fala
recognizer = sr.Recognizer()

# Inicializar o motor de síntese de fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 1.0)  # Volume da fala

def generate_response(input_text):
    """Gera uma resposta usando GPT-3.5 ou GPT-4 via API da OpenAI."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Substitua por "gpt-4" se disponível
            messages=[
                {"role": "system", "content": "Você é um assistente útil e amigável."},
                {"role": "user", "content": input_text}
            ],
            max_tokens=20,  # Limite de palavras na resposta
            temperature=0.7,  # Controla a criatividade
        )
        return response["choices"][0]["message"]["content"].strip()
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
        audio = recognizer.listen(source)  # Captura o áudio do microfone
        
        try:
            # Converter áudio para texto
            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            
            # Gerar resposta com GPT-3.5 ou GPT-4
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
