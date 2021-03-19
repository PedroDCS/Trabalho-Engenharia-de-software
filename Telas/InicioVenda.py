from tkinter import *
from tkinter import ttk
import Telas.ContinuaVenda
import Conexao.ConexaoBd


class Venda(Frame):

    def __init__(self):
        self.tela_venda = Tk()
        self.tela_venda.geometry("600x400")
        self.tela_venda.title("Operação de Venda")
        self.tela_venda.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_venda, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_produto_label = Label(self.tela_venda, text="Produto:")
        nome_produto_label.place(x=70, y=100)
        self.combo_produtos = ttk.Combobox(self.tela_venda, values=Conexao.ConexaoBd.listar("SELECT prodNome FROM Produtos;"))
        self.combo_produtos.place(x=130, y=100)

        unidade_label = Label(self.tela_venda, text="Unidade:")
        unidade_label.place(x=70, y=160)
        self.combo_unidade = ttk.Combobox(self.tela_venda,
                                          values=["Kg", "Caminhão"])
        self.combo_unidade.place(x=135, y=160)

        continuar = Button(self.tela_venda, text="Continuar", command=self.continua_venda)
        continuar.place(x=150, y=330)
        voltar = Button(self.tela_venda, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_venda.mainloop()

    def continua_venda(self):
        Telas.ContinuaVenda.Venda(self.combo_produtos.get(), self.combo_unidade.get())

    def voltar(self):
        self.tela_venda.destroy()
