import speech_recognition as sr
from gtts import gTTS
import pygame

def reconhece_fala():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Diga o seu nome:")
        audio = reconhecedor.listen(fonte)

    try:
        nome = reconhecedor.recognize_google(audio, language='pt-BR')
        return nome
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao tentar usar o serviço de reconhecimento de fala.")
        return None

def cria_e_reproduz_audio(nome):
    texto = f"{nome} é um belo nome"
    tts = gTTS(texto, lang='pt')
    arquivo_audio = "nome_belo.mp3"
    tts.save(arquivo_audio)

    pygame.mixer.init()
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

nome_detectado = reconhece_fala()
if nome_detectado:
    cria_e_reproduz_audio(nome_detectado)
