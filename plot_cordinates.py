import matplotlib.pyplot as plt
from tkinter import *

x = []
y = []

def bt_click():
    print("bt_click")
    x1=int(ex1.get())
    x2=int(ex2.get())
    y1=int(ey1.get())
    y2=int(ey2.get())
    plt.plot([x1,y1],[x2,y2])
    plt.xlabel('velocidade')
    plt.ylabel('aceleracao')
    plt.show(janela)

janela = Tk()

ex1 = Entry(janela, width=5)
ex1.place(x=100,y=150)

ex2 = Entry(janela, width=5)
ex2.place(x=150,y=150)

ey1 = Entry(janela, width=5)
ey1.place(x=100,y=250)

ey2 = Entry(janela, width=5)
ey2.place(x=150,y=250)

bt = Button(janela, width=10, text="ADD & PLOT", command=bt_click)
bt.place(x=100,y=100)


lb = Label(janela, text="Fala galera!")

lb.place(x=10,y=10)

janela.geometry("500x500+200+200")

janela.mainloop()









