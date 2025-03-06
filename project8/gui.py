import pyautogui
import time
time.sleep(5)
pyautogui.click()
distance = 300
while distance > 10:
  pyautogui.dragRel(distance, 0, duration = 0.2)
  distance = distance - 20
  pyautogui.dragRel(0, distance, duration = 0.2)
  pyautogui.dragRel(-distance, 0, duration = 0.2)
  distance = distance - 20
  pyautogui.dragRel()
  pyautogui.dragRel(0, -distance, duration = 0.2)