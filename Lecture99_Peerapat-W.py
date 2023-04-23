from tkinter import *
import math
def CalBMI(event):
    labelResult.configure(text=format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f'))
    bmi =format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f')
    bmiShow = ""
    if float(bmi) <= 17.9:
        bmiShow = "ผอมเกินไป"
    elif float(bmi) >=18 and float(bmi) <= 22.9:
        bmiShow = "ปกติ"
    elif float(bmi) >=23 and float(bmi) <= 24.9:
        bmiShow = "เริ่มอ้วน"
    elif float(bmi) >=25:
        bmiShow = "อ้วน"
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