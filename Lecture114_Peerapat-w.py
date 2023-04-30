import tkinter as tk
from tkinter import ttk
from typing import DefaultDict
from currency_converter import CurrencyConverter
from datetime import date

current = CurrencyConverter()

main_window = tk.Tk()
main_window.geometry("500x450")
main_window.title("USD History")
main_window.configure(background="#636470")

def calculate_click():
    start_day = select_start_day.get()
    start_month = select_start_month.get()
    start_year = select_start_year.get()
    end_day = select_end_day.get()
    end_month = select_end_month.get()
    end_year = select_end_year.get()
    select_start_date.configure(text=start_day+"-"+start_month+"-"+start_year)
    select_end_date.configure(text=end_day+"-"+end_month+"-"+end_year)
    c = CurrencyConverter()

    try:
        convert_start_jpy = "{0:.2f}".format(c.convert(
            1, 'JPY', 'THB', date=date(int(start_year), int(start_month), int(start_day))))
        start_jpy.configure(text="1 JPY : "+convert_start_jpy+" THB")
        error_start_date.configure(text="")
    except:
        error_start_date.configure(text="no data start")
        start_jpy.configure(text="")
        summarize_THB.configure(text="")
        summarize_percentage.configure(text="")

    try:
        convert_end_jpy = "{0:.2f}".format(c.convert(
            1, 'JPY', 'THB', date=date(int(end_year), int(end_month), int(end_day))))
        end_jpy.configure(text="1 JPY : "+convert_end_jpy+" THB")
        erorr_end_date.configure(text="")
    except:
        erorr_end_date.configure(text="no data end")
        end_jpy.configure(text="")
        summarize_THB.configure(text="")
        summarize_percentage.configure(text="")

    try:
        summarize_total_THB = "{0:.2f}".format(
            float(convert_end_jpy) - float(convert_start_jpy))
        if (summarize_total_THB.startswith("-")):
            summarize_THB.configure(
                text="Summarize "+summarize_total_THB+" THB")
        else:
            summarize_THB.configure(
                text="Summarize +"+summarize_total_THB+" THB")
        summarize_total_percentage = "{0:.2f}".format(
            ((float(convert_end_jpy) - float(convert_start_jpy))/float(convert_start_jpy))*100)
        if (summarize_total_percentage.startswith("-")):
            summarize_percentage.configure(
                text="Summarize "+summarize_total_percentage+" %")
        else:
            summarize_percentage.configure(
                text="Summarize +"+summarize_total_percentage+" %")
    except:
        pass


def exit(event):
    main_window.destroy()


main_window.bind("<Escape>", exit)

head_lebel = tk.Label(main_window, text="JPY History",background='#636470',
                      foreground='white', font=('prompt', 22, 'bold'))
head_lebel.place(x=150, y=30, width=200, height=40)

start_date = tk.Label(main_window, text="select start date", background='#24242c',
                      foreground='white', font=('prompt', 16))
start_date.place(x=50, y=100, width=200, height=30)

end_date = tk.Label(main_window, text="select end date", background='#24242c',
                    foreground='white', font=('prompt', 16))
end_date.place(x=280, y=100, width=200, height=30)

select_start_day = ttk.Combobox(main_window, width=2)
select_start_day['values'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
                              "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
select_start_day.place(x=70, y=140)

select_start_month = ttk.Combobox(main_window, width=2)
select_start_month['values'] = (
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
select_start_month.place(x=110, y=140)

select_start_year = ttk.Combobox(main_window, width=4)
select_start_year['values'] = ("2005", "2006", "2007", "2008", "2009", "2010", "2011",
                               "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021","2022")
select_start_year.place(x=150, y=140)

select_end_day = ttk.Combobox(main_window, width=2)
select_end_day['values'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
                            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
select_end_day.place(x=305, y=140)

select_end_month = ttk.Combobox(main_window, width=2)
select_end_month['values'] = (
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
select_end_month.place(x=345, y=140)

select_end_year = ttk.Combobox(main_window, width=4)
select_end_year['values'] = ("2005", "2006", "2007", "2008", "2009", "2010", "2011",
                             "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021","2022")
select_end_year.place(x=385, y=140)

calculate_button = ttk.Button(main_window, text="Calculate", cursor="hand2", style=(
    "success.TButton"), command=calculate_click)
calculate_button.place(x=170, y=180, width=160, height=40)

error_start_date = tk.Label(
    main_window, text="", background="#C0C0C0", fg="red")
error_start_date.place(x=85, y=240, width=100)

erorr_end_date = tk.Label(main_window, text="", background="#C0C0C0", fg="red")
erorr_end_date.place(x=315, y=240, width=100)

select_start_date = tk.Label(main_window, text="")
select_start_date.place(x=85, y=260, width=100)

select_end_date = tk.Label(main_window, text="")
select_end_date.place(x=315, y=260, width=100)

start_jpy = tk.Label(main_window, text="")
start_jpy.place(x=85, y=300, width=100)

end_jpy = tk.Label(main_window, text="")
end_jpy.place(x=315, y=300, width=100)

summarize_THB = tk.Label(main_window, text="")
summarize_THB.place(x=170, y=350, width=160)

summarize_percentage = tk.Label(main_window, text="")
summarize_percentage.place(x=170, y=380, width=160)

main_window.mainloop()