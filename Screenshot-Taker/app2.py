import pyscreenshot
import tkinter as tk

root = tk.Tk()
root.title("Screenshot taker")
canvas1 = tk.Canvas(root,width=300,height=300)
canvas1.pack()

def myScreenshot():
    image = pyscreenshot.grab() 
  
# To view the screenshot 
    image.show() 
  
# To save the screenshot 
    image.save("GeeksforGeeks.png") 

myButton = tk.Button(text = "Take screenshot" , command = myScreenshot , bg = 'green',fg = 'white',font=15)
canvas1.create_window(150,150,window=myButton)


root.mainloop()
