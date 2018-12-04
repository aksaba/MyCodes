import subprocess
import pyautogui
import time
import requests

loginurl ='https://www.reddit.com/login'

subprocess.Popen(['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe','https://www.reddit.com/r/soccer/new/'])
time.sleep(10);
for i in range(100):
    time.sleep(2);
    pyautogui.moveTo(800, 600)
    pyautogui.scroll(-25)
    i = i +1
    print(i)
