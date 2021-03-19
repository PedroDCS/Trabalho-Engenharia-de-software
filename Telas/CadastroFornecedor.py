from tkinter import *

nome_fornecedor_cadastro = StringVar
endereco_fornecedor_cadastro = StringVar
telefone_fornecedor_cadastro = StringVar
cnpj_fornecedor_cadastro = StringVar

class CadastroFornecedor(Frame):

    def __init__(self):
        self.tela_cadastro_fornecedor = Tk()
        self.tela_cadastro_fornecedor.title("Cadastro Fornecedor")
        self.tela_cadastro_fornecedor.geometry("600x400")
        self.tela_cadastro_fornecedor.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cadastro_fornecedor, width=800, height=500, background='#ccd7ff')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_fornecedor_label = Label(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, activebackground='white', font='Bahnschrift',  bd=0, text="Nome do Fornecedor")
        nome_fornecedor_label.place(x=80, y=100)

        nome_fornecedor_entrada = Entry(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, font='Bahnschrift',  bd=0, textvar=nome_fornecedor_cadastro)
        nome_fornecedor_entrada.place(x=300, y=100)
#####################################################
        endereco_fornecedor_label = Label(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, activebackground='white', font='Bahnschrift',  bd=0, text="Endereço do Fornecedor")
        endereco_fornecedor_label.place(x=80, y=150)

        endereco_fornecedor_entrada = Entry(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, font='Bahnschrift',  bd=0, textvar=endereco_fornecedor_cadastro)
        endereco_fornecedor_entrada.place(x=300, y=150)
####################################################
        telefone_fornecedor_label = Label(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, activebackground='white', font='Bahnschrift',  bd=0, text="Telefone do Fornecedor")
        telefone_fornecedor_label.place(x=80, y=200)

        telefone_fornecedor_entrada = Entry(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, font='Bahnschrift',  bd=0, textvar=telefone_fornecedor_cadastro)
        telefone_fornecedor_entrada.place(x=300, y=200)
####################################################
        CNPJ_fornecedor_label = Label(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, activebackground='white', font='Bahnschrift',  bd=0, text="CNPJ do Fornecedor")
        CNPJ_fornecedor_label.place(x=80, y=250)

        CNPJ_fornecedor_entrada = Entry(self.tela_cadastro_fornecedor, bg="#cad8f4", width=20, font='Bahnschrift',  bd=0, textvar=cnpj_fornecedor_cadastro)
        CNPJ_fornecedor_entrada.place(x=300, y=250)
####################################################

        salvar = Button(self.tela_cadastro_fornecedor, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)

        voltar = Button(self.tela_cadastro_fornecedor, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Voltar" ,command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_cadastro_fornecedor.mainloop()

    def voltar(self):
        self.tela_cadastro_fornecedor.destroy()
