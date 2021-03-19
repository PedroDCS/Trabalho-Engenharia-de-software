from tkinter import *
from tkinter import ttk

nome_cliente_cadastro = StringVar
endereco_cliente_cadastro = StringVar
numero_casa_cliente_cadastro = StringVar
telefone_cliente_cadastro = StringVar
cnpj_cliente_cadastro = StringVar


class CadastroCliente(Frame):

    def __init__(self):
        self.tela_cadastro_cliente = Tk()
        self.tela_cadastro_cliente.title("Cadastro Cliente")
        self.tela_cadastro_cliente.geometry("600x400")
        self.tela_cadastro_cliente.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cadastro_cliente, width=800, height=500, background='#ccd7ff')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_cliente_label = Label(self.tela_cadastro_cliente, text="Nome do Cliente", width=15)
        nome_cliente_label.place(x=70, y=70)

        nome_cliente_entrada = Entry(self.tela_cadastro_cliente, textvar=nome_cliente_cadastro)
        nome_cliente_entrada.place(x=200, y=70)
        #####################################################
        endereco_cliente_label = Label(self.tela_cadastro_cliente, text="Rua do Cliente", width=15)
        endereco_cliente_label.place(x=70, y=110)

        combo_rua = ttk.Combobox(self.tela_cadastro_cliente,
                                 values=["Aqui vem uma",
                                         "query SQL",
                                         "que mostra",
                                         "as opções"])
        combo_rua.place(x=200, y=110)

        # endereco_cliente_entrada = Entry(tela_cadastro_cliente, textvar=endereco_cliente_cadastro)
        # endereco_cliente_entrada.place(x=200, y=110)
        ####################################################

        numero_casa_cliente_label = Label(self.tela_cadastro_cliente, text="Nº da Casa", width=15)
        numero_casa_cliente_label.place(x=70, y=150)

        numero_casa_cliente_entrada = Entry(self.tela_cadastro_cliente, textvar=numero_casa_cliente_cadastro)
        numero_casa_cliente_entrada.place(x=200, y=150)
        ####################################################
        telefone_cliente_label = Label(self.tela_cadastro_cliente, text="Telefone do Cliente", width=15)
        telefone_cliente_label.place(x=70, y=190)

        telefone_cliente_entrada = Entry(self.tela_cadastro_cliente, textvar=telefone_cliente_cadastro)
        telefone_cliente_entrada.place(x=200, y=190)
        ####################################################
        CPF_cliente_label = Label(self.tela_cadastro_cliente, text="CPF do Cliente", width=15)
        CPF_cliente_label.place(x=70, y=230)

        CPF_cliente_entrada = Entry(self.tela_cadastro_cliente, textvar=cnpj_cliente_cadastro)
        CPF_cliente_entrada.place(x=200, y=230)
        ####################################################

        salvar = Button(self.tela_cadastro_cliente, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)

        voltar = Button(self.tela_cadastro_cliente, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=330)

        self.tela_cadastro_cliente.mainloop()

    def voltar(self):
        self.tela_cadastro_cliente.destroy()
