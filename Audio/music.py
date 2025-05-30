import pyttsx3
import pygame
import time

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower(): 
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150) 
engine.setProperty('volume', 1.0) 

pygame.mixer.init()

pygame.mixer.music.load("musica.mp3") 
pygame.mixer.music.set_volume(0.3) 
pygame.mixer.music.play()

time.sleep(5)

text_to_speak = (
"Repertório novo no Barão fininho!"
"Respeita fia!"
"Solta o som do paredão papai..."
"Eu prometi não mais te procurar..."
"Mas hoje não é meu dia de sorte..."
"Achei sua foto no meu celular..."
"Não te esqueci, me diz como é que pode..."
"Você me tirou do coração..."
"E eu não te tirei da mente..."
"O álcool não apaga..."
"A saudade da gente, amor, amor..."
"Já que me ensinou a beber..."
"Já que me ensinou a sofrer..."
"Me ensina, por favor!"
"Como é que faz pra te esquecer..."
"Já que me ensinou a beber..."
"Já que me ensinou a sofrer..."
"Me ensina, por favor!"
"Como é que faz pra te esquecer..."
"Rapaziada de São Paulo, galera do Maranhão..."
"Tamo junto..."
"Abre o som do paredão e bota Barão pra tocar, papai..."
"Eu prometi não mais te procurar..."
"Mas hoje não é meu dia de sorte..."
"Achei sua foto no meu celular..."
"Não te esqueci, me diz como é que pode..."
"Você me tirou do coração..."
"E eu não te tirei da mente..."
"O álcool não apaga..."
"A saudade da gente, amor, amor..."
"Já que me ensinou a beber..."
"Já que me ensinou a sofrer..."
"Me ensina, por favor!"
"Como é que faz pra te esquecer..."
"Já que me ensinou a beber..."
"Já que me ensinou a sofrer..."
"Me ensina, por favor!"
"Como é que faz pra te esquecer..."
)

def speak_text(text):
    """Converter texto em fala enquanto a música toca."""
    engine.say(text)
    engine.runAndWait()

speak_text(text_to_speak)

while pygame.mixer.music.get_busy():
    time.sleep(1) 

pygame.mixer.music.stop()
pygame.mixer.quit()
print("Programa encerrado.")
