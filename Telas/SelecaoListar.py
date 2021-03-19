from tkinter import *
import Telas.ListarCliente
import Telas.Cad_Rua
import Telas.Cad_Bairro
import Telas.CadastroCliente
import Telas.CadastroMercadoria


class SelecaoListar(Frame):

    def __init__(self):
        self.tela_selecao_listar = Tk()
        self.tela_selecao_listar.title("Seleção")
        self.tela_selecao_listar.geometry("600x300")
        self.tela_selecao_listar.configure(background='#ccd7ff')

        caixa_canvas = Canvas(self.tela_selecao_listar, width=800, height=500, background='#ccd7ff')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        botao_listar_fornecedores = Button(self.tela_selecao_listar, text="Listar Fornecedor",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0)
        botao_listar_fornecedores.place(x=110, y=60)

        botao_cadastro_mercadorias = Button(self.tela_selecao_listar, text="Listar Mercadoria", bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0)
        botao_cadastro_mercadorias.place(x=110, y=110)

        botao_cadastro_clientes = Button(self.tela_selecao_listar, text="Listar Clientes",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaListarCliente)
        botao_cadastro_clientes.place(x=110, y=160)

        botao_cadastro_rua = Button(self.tela_selecao_listar, text="Listar Venda",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0)
        botao_cadastro_rua.place(x=320, y=60)

        voltar = Button(self.tela_selecao_listar, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=230)

        self.tela_selecao_listar.mainloop()
        self.tela_selecao_listar.destroy()

    def ChamaListarCliente(self):
        Telas.ListarCliente.ListarCliente()

    def voltar(self):
        self.tela_selecao_listar.destroy()
