from tkinter import *

def leftClickButton(event):
    print("Left Click!!")

def doubleClickButton(event):
    print("Double Click!!")

main = Tk()
button = Button(main,text="My Button !!")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-1>',doubleClickButton)
main.mainloop()