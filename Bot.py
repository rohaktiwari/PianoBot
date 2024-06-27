from pyautogui import * 
import pyautogui
import win32con, win32api
import keyboard
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(510,500)[0] == 0:
        click(510,500)
    if pyautogui.pixel(638,500)[0] == 0:
        click(638,500)
    if pyautogui.pixel(368,500)[0] == 0:
        click(368,500)
    if pyautogui.pixel(453,500)[0] == 0:
       click(453,500)

