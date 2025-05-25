import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Listar todas as vozes
for index, voice in enumerate(voices):
    print(f"Voz {index}: {voice.name} - {voice.id}")
