import pyautogui
import time


msg = input("EAM")
n = input("How many times ?: ")

time.sleep(2)

for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')