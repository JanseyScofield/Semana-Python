import time
import yfinance
import pyautogui
import pyperclip
import webbrowser

acao = "PETR4.SA"
dados = yfinance.Ticker(acao).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima  = round(fechamento.max(),2)
minima  = round(fechamento.min(),2)
media  = round(fechamento.mean(),2)

destinatario = "janseymas40@gmail.com"
assunto = "Análise projetos 2020"
mensagem = f"""
Prezado Gestor,

Seguem as análises da ação {acao}:

Máxima : R$ {maxima};
Média : R$ {media};
Mínima : R$ {minima}

Ass: Jansey Scofield da Silva Filho.
"""

pyautogui.PAUSE = 3
webbrowser.open("www.gmail.com")
time.sleep(10)
pyautogui.click(x=168, y=179)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.press("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyautogui.press("enter")
