# Download and install google tesseract OCR
# by this link https://github.com/UB-Mannheim/tesseract/wiki
# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Users\sk\AppData\Local\Tesseract-OCR\tesseract.exe' #put here full path with exe from your system
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #put here full path with exe
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
import random
import pyperclip
import pyautogui
try:
    img=Image.open('test.png')
    x= tess.image_to_string(img)
    print(x)
    pyperclip.copy(x)#after gettubg text it will be copied in your system clipboard
except Exception as e:
    print(e)