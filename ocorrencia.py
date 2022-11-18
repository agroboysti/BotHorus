

import pyautogui as py
import time
from datetime import datetime


time.sleep(5)

BtnOcorrencia1 = py.locateCenterOnScreen("fotos/ocorrencia1.png",confidence=0.5)
print(BtnOcorrencia1)
py.moveTo(BtnOcorrencia1)
py.click()
py.write("http://app.smarteches.com.br/ocorrencias")
py.press("enter")

time.sleep(4)

Btn0t = py.locateCenterOnScreen("fotos/buscar0t.png")
py.moveTo(Btn0t)
py.click()
py.write("sti 0t")
dataAtual = datetime.today()
dataAtual = dataAtual.strftime('%d%m%Y%H%M ')
screenshot = py.screenshot()
screenshot.save("log/"%(dataAtual)%".png")







