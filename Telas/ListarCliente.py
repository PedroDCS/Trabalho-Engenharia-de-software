from tkinter import *
import Conexao.ConexaoBd


class ListarCliente(Frame):

    def __init__(self):
        self.tela_listar_cliente = Tk()
        self.tela_listar_cliente.title("Cadastro Cliente")
        self.tela_listar_cliente.geometry("600x400")
        self.tela_listar_cliente.configure(background='#D3D3D3')

        self.tela_listar_cliente.geometry("600x450+393+133")
        self.tela_listar_cliente.title("Listar Cliente")
        self.tela_listar_cliente.configure(background="#bfbfff")
        self.tela_listar_cliente.configure(highlightcolor="black")

        self.Listbox1 = Listbox(self.tela_listar_cliente)
        self.Listbox1.place(relx=0.05, rely=0.044, relheight=0.818
                            , relwidth=0.907)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(width=544)

        clientes = []
        clientes = Conexao.ConexaoBd.listar("SELECT cliNome, cliTelefone FROM Cliente")

        # opcoes = ["Nome", "Telefone"]
        # self.Listbox1.insert(0, opcoes)

        for i, cliente in enumerate(clientes):
            self.Listbox1.insert(i + 1, cliente)


        self.Button1 = Button(self.tela_listar_cliente)
        self.Button1.place(relx=0.85, rely=0.911, height=31, width=67)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(state='active')
        self.Button1.configure(text='Voltar', command=self.voltar)

        self.tela_listar_cliente.mainloop()

    def voltar(self):
        self.tela_listar_cliente.destroy()
