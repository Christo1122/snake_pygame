import pyautogui as pag
import time
opt = input()

if(opt == 1):
	limit=input("enter the no. of messages")
	msg = input('enter the message')
	i =0

	time.sleep(8)
	while(i<=limit):
		pag.typewrite(msg)
		pag.press('Enter')
		i += 1
if(opt == 2):
	print(pag.position())