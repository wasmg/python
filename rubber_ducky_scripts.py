from ctypes import pythonapi
from typing import Type
import pyautogui
import time

#1 script 

pyautogui.hotkey("win","r")
pyautogui.typewrite("notepad")
pyautogui.hotkey("enter")
time.sleep(1.0)
pyautogui.hotkey("ctrl","s")
pyautogui.typewrite("saniYa")
time.sleep(1.0)
pyautogui.hotkey("enter")
time.sleep(0.9)
pyautogui.hotkey("ctrl","s")
pyautogui.typewrite("saniya is back")
pyautogui.hotkey("enter")
time.sleep(1.0)
pyautogui.hotkey("ctrl","s")
time.sleep(1.0)
pyautogui.hotkey("alt","f4")
pyautogui.hotkey("win","r")
pyautogui.typewrite("cmd")
pyautogui.hotkey("enter")
time.sleep(1.0)
pyautogui.typewrite("color a")
pyautogui.hotkey("enter")
time.sleep(0.9)
pyautogui.typewrite("dir/s")
pyautogui.hotkey("enter")
time.sleep(1.9)
pyautogui.hotkey("alt","f4")
time.sleep(1.0)
pyautogui.click(button="right")
time.sleep(1.0)
pyautogui.moveTo(x=5,y=10)
pyautogui.click()
pyautogui.click()
