from tkinter import *
from tkinter import messagebox

def click():
    nominals = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    res = 0
    for i in range(len(denom)):
        a = f"txt_{i}"
        try:
            num = int(globals()[a]. get())
        except ValueError:
            num = 0 
        res += num * nominals[i]


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
