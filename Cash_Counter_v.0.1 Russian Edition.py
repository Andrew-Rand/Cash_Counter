from tkinter import *


NOMINALS = (0.01, 0.02, 0.05, 0.10, 0.20, 0.50,
            1, 2, 5, 10, 20, 50, 100, 200, 500)

DENOM = ("1 копейка", "2 копейки", "5 копеек", "10 копеек",
         "20 копеек", "50 копеек", 
         "1 рубль", "2 рубля", "5 рублей", "10 рублей",
         "20 рублей", "50 рублей", "100 рублей",
         "200 рублей", "500 рублей")

RUBLES = {0: "рублей",
          1: "рубль",
          2: "рубля",
          3: "рубля",
          4: "рубля",
          5: "рублей",
          6: "рублей",
          7: "рублей",
          8: "рублей",
          9: "рублей"
          }

COP = {0: "копеек",
       1: "копейка",
       2: "копейки",
       3: "копейки",
       4: "копейки",
       5: "копеек",
       6: "копеек",
       7: "копеек",
       8: "копеек",
       9: "копеек"
       }


def count_cash():
    """
        count_cash() scans input fields, calculates cash and whrites
        result to res label
    """
    
    res = 0
    res_rub = 0
    res_cop = 0
    for i in range(len(DENOM)):
        a = f"txt_{i}"
        try:
            num = int(entry_vars_dict[a].get())
        except ValueError:
            num = 0 
        res += num * NOMINALS[i]
        res_rub = int(res // 1)
        res_cop = round((res % 1) * 100)
    result.configure(text=f"В кассе: {res_rub} "
                     f"{RUBLES[int(str(res_rub)[-1])]},"
                     f"{res_cop} {COP[int(str(res_cop)[-1])]}".center(55, " "))


def click():
    """
        after pushing the clear_button
        cash fields will be cleared
    """
    
    for i in range(len(DENOM)):
        a = f"txt_{i}"
        entry_vars_dict[a].delete(0, END)


window = Tk()
window.title("Добро пожаловать в приложение")
window.geometry('350x370')

lbl = Label(window, text="", font=("Arial", 20))
lbl.grid(column=0, row=0)

entry_vars_dict = {}

for i in range(len(DENOM)):
    a = f"txt_{i}"
    if i < (len(DENOM) / 2):
        col_const = 1
        row_const = 1
    else:
        col_const = 4
        row_const = 1 - len(DENOM) // 2
        
    lbl = Label(window, text=DENOM[i], font=("Comic Sans MS", 10))
    lbl.grid(column=col_const, row=i + row_const)
    entry_vars_dict[a] = Entry(window, width=10)
    entry_vars_dict[a].grid(column=1 + col_const, row=i + row_const)


empt = Label(window, text="        ")
empt.grid(column=3, row=10)

result = Label(window, text="", font=("Comic Sans MS", 11))
result.place(x=1, y=270)

clear_btn = Button(window, text="Очистить!",
                   bg="white", fg="red", font=("Comic Sans MS", 10),
                   command=click)
clear_btn.place(x=130, y=320)

while True:
    count_cash()
    window.update_idletasks()
    window.update()
