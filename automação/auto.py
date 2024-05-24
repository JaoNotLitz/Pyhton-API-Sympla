import sys
import os
import pyautogui
import time

# Adiciona o caminho para o diretório "Relatorio"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'relatorio')))

# Agora você pode importar do pacote relatorio
from main import txt_content

# Defina a split_flag
split_flag = "split_flag"

# Divida o conteúdo de txt_content em uma lista de eventos usando a split_flag como separador
eventos = txt_content.split(split_flag)

# Crie uma lista para armazenar os eventos formatados como arrays de linhas
eventos_formatados = []



import pyautogui

# Simula a abertura do Bloco de Notas
pyautogui.hotkey("win")
time.sleep(0.5)
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl","t")
time.sleep(0.5)
pyautogui.write("wa.me/[whatsapp number]")
time.sleep(0.5)
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(936,323)
time.sleep(2)
pyautogui.click(930,390)
time.sleep(15)

# Para cada evento, divida-o em linhas e adicione o array de linhas à lista de eventos formatados
for evento in eventos:
    time.sleep(0.5)
    # Remova espaços extras e quebras de linha, e divida o evento em linhas
    linhas_do_evento = [linha.strip() for linha in evento.strip().split('\n') if linha.strip()]
    # Para cada linha do evento, escreva a linha seguida de uma quebra de linha
    for linha in linhas_do_evento:
        pyautogui.write(linha)
        pyautogui.hotkey("ctrl","enter")
        time.sleep(0.1)
    # Após cada evento, insira duas quebras de linha
    pyautogui.press("enter")

# Agora, os eventos foram digitados no Bloco de Notas com uma quebra de linha entre cada linha e duas quebras de linha entre diferentes eventos

