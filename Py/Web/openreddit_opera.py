import subprocess
import pyautogui
import time

subprocess.Popen(['G:\\Opera\\launcher.exe','https://www.reddit.com/r/soccer/new/'])
time.sleep(10);
pyautogui.moveTo(800, 600)
for i in range(100):
    time.sleep(2);
    pyautogui.scroll(-45)
    i = i +1
    print i
