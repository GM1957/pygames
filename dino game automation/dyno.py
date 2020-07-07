import pyautogui
import pyscreenshot as ImageGrab
from PIL import Image
import time
from mss import mss
import numpy as np

def Press(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(250,280):
        for j in range(470, 500):
            if(data[i,j] < 100):
                Press("up")
            return True    

    for k in range(250, 320):
        for l in range(300,400):
            if(data[k,l] < 100):
                Press("down")
            return True    
    return False           
  


if __name__ == "__main__":
    time.sleep(4)
    Press("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
       
# time.sleep(4)    
# image = ImageGrab.grab().convert('L')
# data = image.load()        
# for i in range(250, 280):
#     for j in range(470, 500):
#         data[i,j] = 0
# for k in range(250, 320):
#     for l in range(300,400):
#         data[k,l] = 0       
# image.show()    
    
