from tkinter import FALSE
import pyautogui,time

time.sleep(3)
pyautogui.FAILSAFE=FALSE

pyautogui.press("win")
time.sleep(2)
pyautogui.press("e")
time.sleep(1)
pyautogui.press("d")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.typewrite("benz avtr")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)