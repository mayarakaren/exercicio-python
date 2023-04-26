from tkinter import *
from tkinter import ttk
import subprocess


tela = Tk()
tela.title("Gestão Escolar")


tela.geometry("750x500")
tela.resizable(True, True)
tela.configure(background="#ffffff")
largura = 700
altura = 350

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#-----------------------------------------------------------------------------------------

lbl_tit = Label(tela, text="Gestão Escolar", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

lbl_codigo = Label(tela, text="Código da Disciplina:", bg="#ffffff").place(x=10, y=140)
txt_codigo = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=130, y=140)
txt_codigo.insert(0, "")

lbl_nome = Label(tela, text="Nome da Disciplina:", bg="#ffffff").place(x=300, y=140)
txt_nome = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=420, y=140)
txt_nome.insert(0, "")

lbl_prof = Label(tela, text="Professor da Disciplina:", bg="#ffffff").place(x=10, y=170)
txt_prof = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_prof.place(x=150, y=170)
txt_prof.insert(0, "")

Label(tela, text="Período da Disciplina:", bg="#ffffff").place(x=300, y=170)

periodo = StringVar()
periodo.set("matutino")

rdb_buttonm = Radiobutton(tela, text="Matutino", variable="var", value="matutino", bg="#ffffff")
rdb_buttonv = Radiobutton(tela, text="Vespertino", variable="var", value="vespertino", bg="#ffffff")
rdb_buttonn = Radiobutton(tela, text="Noturno", variable="var", value="noturno", bg="#ffffff")

rdb_buttonm.place(x=420 , y=170)
rdb_buttonv.place(x=500 , y=170)
rdb_buttonn.place(x=590 , y=170)

Label(tela, text="Horário da Disciplina:", bg="#ffffff").place(x=10, y=200)
comboHorario = ttk.Combobox(tela, 
                            values=[
                                    "08:00", 
                                    "08:50",
                                    "09:40",
                                    "10:30",
                                    "11:20",
                                    "14:00",
                                    "14:50",
                                    "15:40",
                                    "16:30",
                                    "17:20",
                                    "18:10",
                                    "19:00",
                                    "19:50",
                                    "20:40",
                                    "21:30",
                                    "22:20"],)

comboHorario.grid(column=0, row=1)
comboHorario.place(x=130 , y=200)

def abrir_tela_media():
    subprocess.run(["python", "media.py"])



barra_menus = Menu(tela)
opcoes_menus_media = Menu(barra_menus)

barra_menus.add_cascade(label="Verificar Média", menu=opcoes_menus_media)

opcoes_menus_media.add_command(label="Abrir", command=abrir_tela_media)
opcoes_menus_media.add_separator()
opcoes_menus_media.add_command(label="Sair", command=tela.quit)

tela.config(menu=barra_menus)

btn_salvar = Button(tela, text="Salvar", compound= TOP, bg="#f9e6b3").place(x=130, y=280)
btn_alterar = Button(tela, text="Alterar", compound= TOP, bg="#f9e6b3").place(x=180, y=280)
btn_consultar = Button(tela, text="Consultar", compound= TOP, bg="#f9e6b3").place(x=230, y=280)
btn_media = Button(tela, text="Calcular Média", compound= TOP, bg="#f9e6b3", command=abrir_tela_media).place(x=300, y=280)
btn_excluir = Button(tela, text="Excluir", compound= TOP, bg="#f9e6b3").place(x=400, y=280)
btn_sair = Button(tela, text="Sair", compound= RIGHT, bg="#f9e6b3").place(x=620, y=280)



#-----------------------------------------------------------------------------------------

tela.mainloop()