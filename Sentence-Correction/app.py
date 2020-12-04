import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Sentence Correction App')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Sentence:',font=('timesnewroman',13,'italic'))
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root,width=50) 
canvas1.create_window(200, 140, window=entry1)

def getCorrection():
    
    x1 = entry1.get()
    from textblob import TextBlob
    label3 = tk.Label(root, text= 'The Correct Sentence is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
                      
    text1 = TextBlob(x1)
    text1 = text1.correct()
    
    label4 = tk.Label(root, text= text1,font=('helvetica', 14, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Correct', command=getCorrection, bg='brown', fg='black', font=('helvetica', 14, 'bold'))
canvas1.create_window(200, 200, window=button1)
root.mainloop()
