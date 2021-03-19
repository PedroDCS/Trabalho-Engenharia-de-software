from tkinter import *


total_vendas = float
saldo_inicial = float
saldo_final = float


class Fechamento_Caixa(Frame):

    def __init__(self):
        self.tela_fechamento_caixa = Tk()
        self.tela_fechamento_caixa.title("Fechamento Caixa")
        self.tela_fechamento_caixa.geometry("600x350")
        self.tela_fechamento_caixa.configure(background='#D3D3D3')

        canvas = Canvas(self.tela_fechamento_caixa, width=1366, height=768, background='#ccd7ff')

        r1 = canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        canvas.place(x=0, y=0)

        total_vendas_label = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text="Total de vendas: ")
        total_vendas_label.place(x=70, y=100)

        total_vendas_label2 = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text=total_vendas)
        total_vendas_label2.place(x=320, y=100)


        saldo_inicial_label = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text="Saldo Inicial: ")
        saldo_inicial_label.place(x=70, y=150)

        saldo_inicial_label2 = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text=saldo_inicial)
        saldo_inicial_label2.place(x=320, y=150)


        saldo_final_label = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text="Saldo Final: ")
        saldo_final_label.place(x=70, y=200)

        saldo_final_label2 = Label(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text=saldo_final)
        saldo_final_label2.place(x=320, y=200)

        encerrar_fechamento_caixa = Button(self.tela_fechamento_caixa, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text="Encerrar")
        encerrar_fechamento_caixa.place(x=90, y=250)

        desistir_fechamento_caixa = Button(self.tela_fechamento_caixa, text="Desistir", bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.desistir)
        desistir_fechamento_caixa.place(x=300, y=250)

        self.tela_fechamento_caixa.mainloop()

    def desistir(self):
        self.tela_fechamento_caixa.destroy()