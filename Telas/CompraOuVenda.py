from tkinter import *
import Telas.Compra
import Telas.InicioVenda


class CompraOuVenda(Frame):
    def __init__(self):
        self.tela_compra_ou_venda = Tk()
        self.tela_compra_ou_venda.geometry("600x250")
        self.tela_compra_ou_venda.title("Compra ou Venda")
        self.tela_compra_ou_venda.configure(background='#ccd7ff')

        caixa_canvas = Canvas(self.tela_compra_ou_venda, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 170, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        bt1 = Button(self.tela_compra_ou_venda, text="Comprar Materiais", bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCompra)
        bt1.place(x=80, y=100)
        bt2 = Button(self.tela_compra_ou_venda, text="Vender Materiais", bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaVenda)
        bt2.place(x=320, y=100)

        voltar = Button(self.tela_compra_ou_venda, bg="#cad8f4", width=14, activebackground='white', font='Bahnschrift',  bd=0, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=360, y=190)

        self.tela_compra_ou_venda.mainloop()

    def voltar(self):
        self.tela_compra_ou_venda.destroy()

    def ChamaCompra(self):
        Telas.Compra.Compra()

    def ChamaVenda(self):
        Telas.InicioVenda.Venda()
