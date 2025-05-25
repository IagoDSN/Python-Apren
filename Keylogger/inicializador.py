import os
import shutil
from win32com.client import Dispatch

caminho_exe = r"COM.exe"

pasta_inicializacao = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

nome_atalho = "Microsoft.lnk"

caminho_atalho = os.path.join(pasta_inicializacao, nome_atalho)

shell = Dispatch('WScript.Shell')
atalho = shell.CreateShortcut(caminho_atalho)
atalho.TargetPath = caminho_exe
atalho.WorkingDirectory = os.path.dirname(caminho_exe)
atalho.Save()

print(f"Atalho criado em: {caminho_atalho}")
