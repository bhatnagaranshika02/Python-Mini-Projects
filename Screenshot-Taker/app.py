import pyautogui
import tkinter as tk

root = tk.Tk()
root.title("Screenshot taker")
canvas1 = tk.Canvas(root,width=300,height=300)
canvas.pack()

def myScreenshot():
    sc = pyautogui.screenshot()
    sc.save(r'C:\Python\Screenshot\screenshot1')

    myButton = tk.Button(text = "Take screenshot" , command = myScreenshot , bg = 'green',fg = 'white',font=15)
    canvas.create_window(150,150,window=myButton)


root.mainloop()
