#Screenshot App with Python

#pakages needed
import pyautogui
import time
import tkinter as tk

#screenshot function
def screenshot():
    Picture_name= int(round(time.time() *1000))
    #change the path to your own directory
    Picture_name= 'screenshot-data/{}.png'.format(Picture_name)
    time.sleep(3)   #delay time 3 seconds
    img = pyautogui.screenshot(Picture_name)
    img.show()

#Codes for the GUI , creating the GUI window
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
#canvas1=tk.Canvas(root,width=30, height=25)
#canvas1.pack()


#Screenshot Button
button=tk.Button(
    frame,
    text = "Take Screenshot" , 
    command=screenshot)

#Quit Button
button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text="QUIT" ,
    command=quit)
close.pack(side=tk.LEFT)


root.mainloop()