import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga 'porta' para continuar...")
    
    while True:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            
            if text.lower() == "sair":
                print("prosseguindo...")
                break
            else:
                print("Palavra não reconhecida, tente novamente.")
        
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
        except sr.RequestError as e:
            print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))

print("Programa finalizado.")