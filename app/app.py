import pyperclip
import tkinter as tk
from PIL import Image, ImageTk
from plano import get_ai_response, check_clipboard 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App Coragem o cão")
        self.geometry("400x300")
        self.minsize(280, 160)
        self.maxsize(280, 160)

        self.ai_response = tk.StringVar()
        self.last_text = ""

        self.bg_image = Image.open("courage.jfif")
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = tk.Label(self, textvariable=self.ai_response, bg="white")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Ativar Coragem", command=self.activate_ai, bg="green")
        self.button.pack(pady=10)

        self.active = False

    def activate_ai(self):
        self.active = not self.active
        if self.active:
            self.button.config(bg="red", text="Desativar")
            self.after(1000, self.check_clipboard_wrapper)
        else:
            self.button.config(bg="green", text="Ativar")

    def check_clipboard_wrapper(self):
        check_clipboard(self)

app = App()
app.mainloop()
