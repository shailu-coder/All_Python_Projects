# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query main page- https://www.instagram.com/python_Coderz_/
# My Facebook - https://www.facebook.com/shailendrakr007
# My Instagram - https://www.instagram.com/shailendra_kr_007/

"""Watch video before using it
https://www.youtube.com/watch?v=xVR-8xuBp3k"""

import webbrowser
import pyautogui
import time


person_name = input('Enter The Person Name Whom You Want To Send A Message: ')
my_msg = input('Enter Your Message: ')

webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
print(pyautogui.position())

# click on search bar
pyautogui.click(184,189)
pyautogui.typewrite(person_name)


time.sleep(5)

#click on person 
pyautogui.click(163,319)

time.sleep(5)

pyautogui.typewrite(my_msg)

time.sleep(2)
pyautogui.click(1332,692) # click on Send button

