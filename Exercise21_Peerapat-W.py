from tkinter import *
import math
def CalBMI(event):
    labelResult.configure(text=format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f'))
    bmi =format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f')
    bmiShow = ""
    if float(bmi) <= 18.5:
        bmiShow = "ผอมเกินไป"
    elif float(bmi) >=18.6 and float(bmi) <= 22.9:
        bmiShow = "น้ำหนักปกติ"
    elif float(bmi) >=23 and float(bmi) <= 24.9:
        bmiShow = "น้ำหนักเกิน"
    elif float(bmi) >= 25 and float(bmi) <= 29.9:
        bmiShow = "อ้วน"
    elif float(bmi) >=30:
        bmiShow = "อ้วนมาก"
    lableBMI.configure(text=bmiShow)

MainWindow= Tk()
MainWindow.title("BMI")

labelHeight = Label(MainWindow,text="ส่วนสูง (m)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก (kg)")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',CalBMI)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

lableBMI = Label(MainWindow,text=" ")
lableBMI.grid(row=3,column=1)

MainWindow.mainloop()