import pyautogui
import time
import keyboard
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

x=1
while(True):
    if(keyboard.is_pressed('esc')):
        pyautogui.screenshot('C:\\Users\\rauna\\Desktop\\programs\\resumefilling\\image'+str(x)+'.png')
        
        #crop image
        
        #im = Image.open(r'C:\\Users\\rauna\\Desktop\\programs\\resumefilling\\image'+str(x)+'.png')
        #left = 350
        #top = 50
        #right = 900
        #bottom = 1003
        #im1 = im.crop((left, top, right, bottom))
        #im1.save('C:\\Users\\rauna\\Desktop\\programs\\resumefilling\\image'+str(x)+'.png', 'PNG')

        #convert to text
        image=Image.open('image'+str(x)+'.png')
        output=pytesseract.image_to_string(image)
        f = open('image'+str(x)+'.txt', "w")
        f.write(output)
        f.close()
        x=x+1
    elif(keyboard.is_pressed('end')):
        break
    else:
        pass
