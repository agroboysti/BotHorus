import pyautogui, time
from datetime import datetime
time.sleep(1)

dataAtual = datetime.today()
dataAtual = dataAtual.strftime('%d%m%Y%H%M ')
print(dataAtual)

 
screenshot = pyautogui.screenshot()
screenshot.save("dataAtual.png")