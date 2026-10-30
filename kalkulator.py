import tkinter as tk

list = []

def equ():
    equal = "".join(str(x) for x in list)
    wynik = eval(equal)
    print(wynik)
    label.config(text=wynik)
    list.clear()
    list.append(wynik)

def kliknij(x):
    list.append(x)
    print(list)
    label.config(text=list)

def dzialanie(y):
    if len(list) == 0:
        print("nie ma żadnych liczb")
        label.config(text="nie ma żadnych liczb")
    elif type(list[-1]) == str:
        print("error")
        label.config(text="error")
    else:
        kliknij(y)

def clear():
    list.clear()
    print(list)
    label.config(text="")

def kropka():
    if len(list) == 0 or list[-1] == "+" or list[-1] == "-" or list[-1] == "*" or list[-1] == "/":
        list.append(0)
        list.append(".")
    elif type(list[-1]) == int:
        a = 0
        running = True
        while running:
            a -= 1
            print(list[a])
            if list[a] == "+" or list[a] == "-" or list[a] == "*" or list[a] == "/" or a == (len(list) * -1):
                print("działa")
                list.append(".")
                running = False
            elif list[a] == ".":
                print("błąd")
                label.config(text="błąd")
                running = False
    print(list)
    label.config(text=list)

def back():
    list.pop(-1)
    print(list)
    label.config(text=list)


root = tk.Tk()
root.geometry("145x200-1-1")
root.configure(bg="#252525")
root.resizable(False, False)
root.title("Kalkulator")

root.bind("0", lambda event: kliknij(0))
root.bind("1", lambda event: kliknij(1))
root.bind("2", lambda event: kliknij(2))
root.bind("3", lambda event: kliknij(3))
root.bind("4", lambda event: kliknij(4))
root.bind("5", lambda event: kliknij(5))
root.bind("6", lambda event: kliknij(6))
root.bind("7", lambda event: kliknij(7))
root.bind("8", lambda event: kliknij(8))
root.bind("9", lambda event: kliknij(9))

root.bind("+", lambda event: dzialanie("+"))
root.bind("-", lambda event: dzialanie("-"))
root.bind("*", lambda event: dzialanie("*"))
root.bind("/", lambda event: dzialanie("/"))

root.bind(".", lambda event: kropka())

root.bind("<Return>", lambda event: equ())
root.bind("<BackSpace>", lambda event: back())





label = tk.Label(bg="#252525", fg="#ffffff")
btn1 = tk.Button(bg="#454545", text="1", fg="#ffffff", command=lambda: kliknij(1), width=1, height=1)
btn2 = tk.Button(bg="#454545", text="2", fg="#ffffff", command=lambda: kliknij(2), width=1, height=1)
btn3 = tk.Button(bg="#454545", text="3", fg="#ffffff", command=lambda: kliknij(3), width=1, height=1)
btn4 = tk.Button(bg="#454545", text="4", fg="#ffffff", command=lambda: kliknij(4), width=1, height=1)
btn5 = tk.Button(bg="#454545", text="5", fg="#ffffff", command=lambda: kliknij(5), width=1, height=1)
btn6 = tk.Button(bg="#454545", text="6", fg="#ffffff", command=lambda: kliknij(6), width=1, height=1)
btn7 = tk.Button(bg="#454545", text="7", fg="#ffffff", command=lambda: kliknij(7), width=1, height=1)
btn8 = tk.Button(bg="#454545", text="8", fg="#ffffff", command=lambda: kliknij(8), width=1, height=1)
btn9 = tk.Button(bg="#454545", text="9", fg="#ffffff", command=lambda: kliknij(9), width=1, height=1)
btn0 = tk.Button(bg="#454545", text="0", fg="#ffffff", command=lambda: kliknij(0), width=1 , height=1)
btnp = tk.Button(bg="#454545", text="+", fg="#ffffff", command=lambda: dzialanie("+"), width=1, height=1)
btnm = tk.Button(bg="#454545", text="-", fg="#ffffff", command=lambda: dzialanie("-"), width=1, height=1)
btne = tk.Button(bg="#454545", text="=", fg="#ffffff", command=equ, width=1, height=1)
btnr = tk.Button(bg="#454545", text="*", fg="#ffffff", command=lambda: dzialanie("*"), width=1, height=1)
btnn = tk.Button(bg="#454545", text="/", fg="#ffffff", command=lambda: dzialanie("/"), width=1, height=1)
btnc = tk.Button(bg="#454545", text="c", fg="#ffffff", command=clear, width=1, height=1)
btndot = tk.Button(bg="#454545", text=".", fg="#ffffff", command=kropka, width=1, height=1)
btnbac = tk.Button(bg="#454545", text="<-", fg="#ffffff", command=back, width=1, height=1)

label.grid(column=0, row=0, columnspan=4, sticky="ew", padx=5, pady=5)

btnbac.grid(column=2, row=1)
btnc.grid(column=3, row=1)

btn1.grid(column=0, row=2)
btn2.grid(column=1, row=2)
btn3.grid(column=2, row=2)
btnn.grid(column=3, row=2)

btn4.grid(column=0, row=3)
btn5.grid(column=1, row=3)
btn6.grid(column=2, row=3)
btnr.grid(column=3, row=3)

btn7.grid(column=0, row=4)
btn8.grid(column=1, row=4)
btn9.grid(column=2, row=4)
btnm.grid(column=3, row=4)

btn0.grid(column=0, row=5)
btndot.grid(column=1, row=5)
btne.grid(column=2, row=5)
btnp.grid(column=3, row=5)

root.mainloop()
