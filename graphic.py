from tkinter import *

def bt_click():
    print("bt_click")
    lb["text"] = "It Woks!"

janela = Tk()


bt = Button(janela, width=10, text="OK", command=bt_click)
bt.place(x=100,y=100)


lb = Label(janela, text="Fala galera!")

lb.place(x=10,y=10)

janela.geometry("500x200+200+200")

janela.mainloop()