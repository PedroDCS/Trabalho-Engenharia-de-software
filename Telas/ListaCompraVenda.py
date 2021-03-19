from tkinter import *

class Lista_de_compra_e_venda(Frame):
    def __init__(self):
        self.lista_compra_ou_venda = Tk()
        self.lista_compra_ou_venda.geometry("600x400")
        self.lista_compra_ou_venda.title("Listar")
        self.lista_compra_ou_venda.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.lista_compra_ou_venda, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        bt1 = Button(self.lista_compra_ou_venda, text="Listar compras de materiais", width=25)
        bt1.place(x=60, y=150)
        bt2 = Button(self.lista_compra_ou_venda, text="Listar vendas de materiais", width=25)
        bt2.place(x=310, y=150)

        voltar = Button(self.lista_compra_ou_venda, text="Voltar", command=self.voltar)
        voltar.place(x=450, y=330)

        self.lista_compra_ou_venda.mainloop()

    def voltar(self):
        self.lista_compra_ou_venda.destroy()
