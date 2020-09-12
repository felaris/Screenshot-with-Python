#Screenshot App with Python

#pakages needed
import pyautogui
import time


#screenshot function
def screenshot():
    Picture_name= int(round(time.time() *1000))
    #change the path to your own directory
    Picture_name= 'screenshot-data/{}.png'.format(Picture_name)
    time.sleep(3)   #delay time 3 seconds
    img = pyautogui.screenshot(Picture_name)
    img.show()

screenshot()
