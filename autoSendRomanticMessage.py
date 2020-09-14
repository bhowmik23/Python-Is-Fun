import pyautogui
import time
message = 100 # what number you want to sent
while message>0:
    time.sleep(4) #time gap afer sent again
    pyautogui.typewrite("I love you ") # the message you want to sent
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1