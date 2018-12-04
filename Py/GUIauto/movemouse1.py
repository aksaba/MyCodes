import pyautogui
for i in range(10):
	pyautogui.position()
	pyautogui.moveTo(1029, 210, duration=0.15)
	pyautogui.click()
	pyautogui.moveTo(1135, 210, duration=0.15)
	pyautogui.click()
	pyautogui.moveTo(1241, 210, duration=0.15)
	pyautogui.click()
	pyautogui.scroll(128)
