from tkinter import *


import Telas.SelecaoCaixa
import Telas.Estoque
import Telas.Cadastros
import Telas.CompraOuVenda
import Telas.ListaCompraVenda
import Telas.SelecaoListar

valorInicialCaixa = DoubleVar


class Principal(Frame):
    def __init__(self, **kw):
        #super().__init__(**kw)
        tela_bem_vindo = Tk()
        tela_bem_vindo.title("Bem Vindo")
        tela_bem_vindo.geometry("800x500")
        tela_bem_vindo.configure(background='#D3D3D3')

        canvas = Canvas(tela_bem_vindo, width=800, height=500, background='#ccd7ff')

        r1 = canvas.create_rectangle(50, 100, 250, 400, fill="white", outline='red', width=3)
        r2 = canvas.create_rectangle(300, 100, 700, 220, fill="white", outline='red', width=3)
        r3 = canvas.create_rectangle(300, 250, 700, 400, fill="white", outline='red', width=3)

        # img = PhotoImage(file="logo_provisoria2.jpg")
        # canvas.create_image(0, 0, image=img, anchor=NW)

        canvas.place(x=0, y=0)

        #################### bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0

        caixa = Button(tela_bem_vindo, text="Caixa",  bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCaixa)
        caixa.place(x=65, y=150)

        estoque = Button(tela_bem_vindo, text="Estoque", bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaEstoque)
        estoque.place(x=65, y=190)

        pedidos = Button(tela_bem_vindo, text="Compra/Venda", bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCompraVenda)  # ,command=Caixa)
        pedidos.place(x=65, y=230)

        cadastros = Button(tela_bem_vindo, text="Cadastros", bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastros)
        cadastros.place(x=65, y=270)

        recebimentos = Button(tela_bem_vindo, text="Listar", bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaListar)  # ,command=Caixa)
        recebimentos.place(x=65, y=310)
        tela_bem_vindo.mainloop()

    def ChamaCaixa(self):
        Telas.SelecaoCaixa.SelecaoCaixa()

    def ChamaEstoque(self):
        Telas.Estoque.Estoque()

    def ChamaCadastros(self):
        Telas.Cadastros.Cadastros()

    def ChamaCompraVenda(self):
        Telas.CompraOuVenda.CompraOuVenda()

    def ChamaListar(self):
        Telas.SelecaoListar.SelecaoListar()


