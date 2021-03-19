from tkinter import *
from tkinter import ttk

nome_material = StringVar
qtd_material = 0


class Compra(Frame):

    def __init__(self):
        self.tela_compra = Tk()
        self.tela_compra.geometry("600x400")
        self.tela_compra.title("Comprar Materiais")
        self.tela_compra.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_compra, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        ####################################################

        produto_label = Label(self.tela_compra, text="Produto", width=15)
        produto_label.place(x=70, y=60)

        combo_produto = ttk.Combobox(self.tela_compra,
                                     values=["Aqui vem uma",
                                             "query SQL",
                                             "que mostra",
                                             "as opções"])

        combo_produto.place(x=200, y=60)

        ####################################################

        fornecedor_label = Label(self.tela_compra, text="Fornecedor", width=15)
        fornecedor_label.place(x=70, y=90)

        combo_fornecedor = ttk.Combobox(self.tela_compra,
                                        values=["Aqui vem uma",
                                                "query SQL",
                                                "que mostra",
                                                "as opções"])

        combo_fornecedor.place(x=200, y=90)

        ####################################################

        data_label = Label(self.tela_compra, text="Data da compra", width=15)
        data_label.place(x=70, y=120)

        data_entrada = Entry(self.tela_compra)
        data_entrada.place(x=200, y=120)

        ####################################################

        quantidade_label = Label(self.tela_compra, text="Quantidade", width=15)
        quantidade_label.place(x=70, y=150)

        quantidade_entrada = Entry(self.tela_compra)
        quantidade_entrada.place(x=200, y=150)

        ####################################################

        valor_label = Label(self.tela_compra, text="Valor da compra", width=15)
        valor_label.place(x=70, y=180)

        valor_entrada = Entry(self.tela_compra)
        valor_entrada.place(x=200, y=180)

        ####################################################

        status_label = Label(self.tela_compra, text="Estatus da compra", width=15)
        status_label.place(x=70, y=210)

        status_entrada = Entry(self.tela_compra)
        status_entrada.place(x=200,y=210)

        ####################################################

        pagamento_label = Label(self.tela_compra, text="Tipo de Pagamento", width=15)
        pagamento_label.place(x=70, y=240)

        combo_pagamento = ttk.Combobox(self.tela_compra,
                                       values=["Dinheiro",
                                               "Cartão",
                                               "Cheque"])
        combo_pagamento.place(x=200, y=240)

        ####################################################

        descricao_label = Label(self.tela_compra, text="Descrição", width=15)
        descricao_label.place(x=70, y=270)

        descricao_entrada = Entry(self.tela_compra, width=55)
        descricao_entrada.place(x=200,y=270)

        salvar = Button(self.tela_compra, text="Comprar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_compra, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=330)

        self.tela_compra.mainloop()

    def voltar(self):
        self.tela_compra.destroy()