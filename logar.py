

import pyautogui as py
import time
time.sleep(5)
BtnUsuario = py.locateCenterOnScreen("fotos/usuario.png",confidence=0.5)
BtnSenha = py.locateCenterOnScreen("fotos/senha.png",confidence=0.5)
BtnLogin = py.locateCenterOnScreen("fotos/login.png",confidence=0.5)
BtnOcorrencia1 = py.locateCenterOnScreen("fotos/ocorrencia1.png",confidence=0.5)

def Logar():
    py.moveTo(BtnUsuario)
    py.click()
    py.write("gerenciati")
    py.press("tab")
    time.sleep(1)
    py.write("smartech2021")
    time.sleep(1)
    py.moveTo(BtnLogin)
    py.click()

py.moveTo(BtnOcorrencia1)
py.write("http://app.smarteches.com.br/ocorrencias")






