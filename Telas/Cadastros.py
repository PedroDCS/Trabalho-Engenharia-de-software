from tkinter import *
import Telas.CadastroFornecedor
import Telas.Cad_Rua
import Telas.Cad_Bairro
import Telas.CadastroCliente
import Telas.CadastroMercadoria


class Cadastros(Frame):

    def __init__(self):
        self.tela_cadastros = Tk()
        self.tela_cadastros.title("Tela de cadastros")
        self.tela_cadastros.geometry("600x300")
        self.tela_cadastros.configure(background='#ccd7ff')

        caixa_canvas = Canvas(self.tela_cadastros, width=800, height=500, background='#ccd7ff')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        botao_cadastro_fornecedores = Button(self.tela_cadastros, text="Cadastrar Fornecedor",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastroFornecedor)
        botao_cadastro_fornecedores.place(x=110, y=60)

        botao_cadastro_mercadorias = Button(self.tela_cadastros, text="Cadastrar Mercadoria", bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastroMercadoria)
        botao_cadastro_mercadorias.place(x=110, y=110)

        botao_cadastro_clientes = Button(self.tela_cadastros, text="Cadastrar Clientes",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastroCliente)
        botao_cadastro_clientes.place(x=110, y=160)

        botao_cadastro_rua = Button(self.tela_cadastros, text="Cadastrar Rua",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastroRua)
        botao_cadastro_rua.place(x=320, y=60)

        botao_cadastro_bairro = Button(self.tela_cadastros, text="Cadastrar Bairro",  bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, command=self.ChamaCadastroBairro)
        botao_cadastro_bairro.place(x=320, y=110)

        voltar = Button(self.tela_cadastros, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=230)

        self.tela_cadastros.mainloop()
        self.tela_cadastros.destroy()

    def ChamaCadastroFornecedor(self):
        Telas.CadastroFornecedor.CadastroFornecedor()

    def ChamaCadastroRua(self):
        Telas.Cad_Rua.CadastroRua()

    def ChamaCadastroBairro(self):
        Telas.Cad_Bairro.CadastroBairro()

    def ChamaCadastroCliente(self):
        Telas.CadastroCliente.CadastroCliente()

    def ChamaCadastroMercadoria(self):
        Telas.CadastroMercadoria.CadastroMercadoria()



    def voltar(self):
        self.tela_cadastros.destroy()
