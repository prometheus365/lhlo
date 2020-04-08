from tkinter import *

def button():
    if (str(index.get()).isnumeric() and str(número.get()).isnumeric() and str(index.get()) >= '2'):
        ind = float(index.get())
        núm = float(número.get())
        raiz = núm ** (1/ind)
        lb4['text']= raiz
        lb4.place(x=90,y=230)

    else:
        lb4['text']= 'Valores incorretos tente novamente'
        lb4.place(x=40,y=230)

janela = Tk()
lb1= Label(janela, text='RAIZ', font=('arial', -30), foreground= 'white')
lb1['bg']= 'black'
lb1.place(x=120,y=0)

lb2= Label(janela, text='INDEX', foreground= 'white')
lb2['bg']= 'black'
lb2.place(x=90,y=100)

index = Entry(janela)
index.place(x=90,y=120)

lb3= Label(janela, text='NÚMERO', foreground= 'white')
lb3['bg']= 'black'
lb3.place(x=90,y=150)

número = Entry(janela)
número.place(x=90,y=170)

bt= Button(janela, width= 5, text='RAIZ', foreground= 'white', command=button)
bt['bg']= 'black'
bt.place(x=130,y=200)

lb4= Label(janela, font=(20))
lb4['bg']= 'black'
lb4['foreground']= 'white'

janela['bg']= 'black'
janela.resizable(False, False)
janela.geometry('300x300')
janela.title('RAIZ')
janela.mainloop()
