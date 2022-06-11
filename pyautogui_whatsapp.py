import pyautogui, webbrowser
from time import sleep


webbrowser.open('https://web.whatsapp.com/send?phone=+593964091474')
sleep(10)

pyautogui.typewrite('holiiiii')
pyautogui.press('enter')
