import speech_recognition as sr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pyttsx3

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def generate_response(input_text):
    """Gera uma resposta usando GPT-2 com attention_mask e pad_token configurados."""

    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"], 
        max_length=50, 
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=1, 
        top_k=50, 
        top_p=0.95 
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def speak_response(response_text):
    """Converte a resposta em áudio e a reproduz."""
    engine.say(response_text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Fale algo para que o modelo responda...")

    while True:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:

            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            
            response = generate_response(text)
            print("Resposta do modelo: " + response)
            
            speak_response(response)
            
            if text.lower() == "sair":
                print("Encerrando o programa...")
                break 
        
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")

print("Programa finalizado.")
