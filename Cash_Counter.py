from tkinter import *
from tkinter import messagebox

def click():
    res = int(txt_0.get()) * 0.01 + \
        int(txt_1.get()) * 0.02 + \
        int(txt_2.get()) * 0.05 + \
        int(txt_3.get()) * 0.10 + \
        int(txt_4.get()) * 0.20 + \
        int(txt_5.get()) * 0.50 + \
        int(txt_6.get()) * 1 + \
        int(txt_7.get()) * 2 + \
        int(txt_8.get()) * 5 + \
        int(txt_9.get()) * 10 + \
        int(txt_10.get()) * 20 + \
        int(txt_11.get()) * 50 + \
        int(txt_12.get()) * 100 + \
        int(txt_13.get()) * 200 + \
        int(txt_14.get()) * 500 
        
    messagebox.showinfo("Hi!", f"Something was counted {res}")

window = Tk()
window.title("Welcome to application!")
window.geometry('420x300')

lbl = Label(window, text="Hello!", font=("Arial", 15))
lbl.grid(column=0, row=0)

#  Объявление всех ячеек, переделать в ООП!!!

denom = ["1 копейка", "2 копейки", "5 копеек", "10 копеек",
         "20 копеек", "50 копеек", 
         "1 рубль", "2 рубля", "5 рублей", "10 рублей",
         "20 рублей", "50 рублей", "100 рублей",
         "200 рублей", "500 рублей"]


for i in range(len(denom)):
    a = f"txt_{i}"
    if i < (len(denom) / 2):
        lbl = Label(window, text=denom[i])
        lbl.grid(column=1, row= i + 1)
        globals()[a] = Entry(window, width=10)
        globals()[a].grid(column=2, row= i + 1)
    else:
        lbl = Label(window, text=denom[i])
        lbl.grid(column=4, row= i + 1 - len(denom) // 2)
        globals()[a] = Entry(window, width=10)
        globals()[a].grid(column=5, row= i + 1 - len(denom) // 2)

empt = Label(window, text="")
empt.grid(row=10)

btn = Button(window, text="Count!", bg="white", fg="black", command=click)
btn.grid(column=3, row=11)


window.mainloop()

window.mainloop()
