from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

tela = Tk()
tela.title("Gestão Escolar")


tela.geometry("750x500")
tela.resizable(True, True)
tela.configure(background="#ffffff")
largura = 650
altura = 350

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#-----------------------------------------------------------------------------------------


lbl_tit = Label(tela, text="Média", font=("Arial", 30, "bold"), bg="#ffffff").place(x=280, y=50)

lbl_nome = Label(tela, text="Nome da Disciplina:", bg="#ffffff").place(x=10, y=140)
txt_nome = Entry(tela, width=30, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=130, y=140)
txt_nome.insert(0, "")

lbl_prof = Label(tela, text="Professor da Disciplina:", bg="#ffffff").place(x=10, y=170)
txt_prof = Entry(tela, width=30, borderwidth=2, fg="black", bg="white")
txt_prof.place(x=140, y=170)
txt_prof.insert(0, "")

lbl_n1 = Label(tela, text="Digite a nota 1:", bg="#ffffff").place(x=10, y=200)
txt_n1 = Entry(tela, width=30, borderwidth=2, fg="blue", bg="white") 
txt_n1.pack()
txt_n1.place(x=100, y=200)
txt_n1.insert(0, "n1")

lbl_n2 = Label(tela, text="Digite a nota 2", bg="#ffffff").place(x=10, y=230)
txt_n2 = Entry(tela, width=30, borderwidth=2, fg="blue", bg="white")
txt_n2.pack()
txt_n2.place(x=100, y=230)
txt_n2.insert(0, "n2")

lbl_n3 = Label(tela, text="Digite a nota 3", bg="#ffffff").place(x=10, y=260)
txt_n3 = Entry(tela, width=30, borderwidth=2, fg="blue", bg="white")
txt_n3.pack()
txt_n3.place(x=100, y=260)
txt_n3.insert(0, "n3")

def click() :

    n1 = float(txt_n1.get())
    n2 = float(txt_n2.get())
    n3 = float(txt_n3.get())

    calc= n1 * 0.5 + n2 * 0.3 + n3 * 0.2/3

    if calc >= 6:
        print("Aluno Aprovado! e a Média do aluno é:")
        print(calc)
        messagebox.showinfo('Média', 'Aluno aprovado!')
    else: 
        print("Aluno Reprovado! e a Média do aluno é;")
        print(calc)
        messagebox.showinfo('Média', 'Aluno reprovado!')

btn_calc = Button(tela, text="Calcular Média", compound= TOP, bg="#f9e6b3", command=click).place(x=550, y=300)


#-----------------------------------------------------------------------------------------

tela.mainloop()