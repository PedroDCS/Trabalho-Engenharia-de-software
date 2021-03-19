from tkinter import *
from tkinter import ttk
import Conexao.ConexaoBd
from datetime import date


class Venda:
    def __init__(self, produto, unidade):
        self.tela_venda2 = Tk()
        self.tela_venda2.geometry("700x500")
        self.tela_venda2.title("Operação de Venda")
        self.tela_venda2.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_venda2, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 650, 400, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_rua_label = Label(self.tela_venda2, text="Tipo produto:")
        nome_rua_label.place(x=70, y=80)
        combo_unidade = ttk.Combobox(self.tela_venda2, values=Conexao.ConexaoBd.listar("SELECT tipNome FROM Tipo;"))
        combo_unidade.place(x=160, y=80)

        if unidade == 'Caminhão':
            unidade_label = Label(self.tela_venda2, text="Nº caminhões:")
            unidade_label.place(x=70, y=120)
            unidade_entrada = Entry(self.tela_venda2)
            unidade_entrada.place(x=170, y=120)
        else:
            unidade_label = Label(self.tela_venda2, text="Quantidade(Kg):")
            unidade_label.place(x=70, y=120)
            unidade_entrada = Entry(self.tela_venda2)
            unidade_entrada.place(x=180, y=120)

        pagamento_label = Label(self.tela_venda2, text="Pagamento:")
        pagamento_label.place(x=70, y=160)
        self.combo_pag = ttk.Combobox(self.tela_venda2, values=Conexao.ConexaoBd.listar("SELECT tpaNome FROM Tipo_Pagamento;"))
        self.combo_pag.place(x=150, y=160)

        data_label = Label(self.tela_venda2, text="Data da venda:")
        data_label.place(x=70, y=200)
        self.data_venda = Entry(self.tela_venda2)
        self.data_venda.place(x=170, y=200)
        self.data_venda.insert(0, self.retorna_data())

        cliente_label = Label(self.tela_venda2, text="Cliente:")
        cliente_label.place(x=70, y=240)
        self.combo_cliente = ttk.Combobox(self.tela_venda2, values=Conexao.ConexaoBd.listar("SELECT cliNome FROM Cliente;"))
        self.combo_cliente.place(x=123, y=240)

        status_label = Label(self.tela_venda2, text="Está venda já foi paga?")
        status_label.place(x=390, y=80)
        self.combo_status = ttk.Combobox(self.tela_venda2,
                                      values=["Sim", "Não"])
        self.combo_status.place(x=390, y=110)

        self.check_box = IntVar()
        self.c = Checkbutton(self.tela_venda2, text="Venda já foi entregue", variable=self.check_box)
        self.c.place(x=390, y=160)

        descricao_label = Label(self.tela_venda2, text="Descrição:")
        descricao_label.place(x=390, y=220)
        self.descricao = Text(self.tela_venda2, height=8, width=30)
        self.descricao.place(x=390, y=250)

        total_label = Label(self.tela_venda2, text="Total(R$):")
        total_label.place(x=70, y=360)
        total_saida = Entry(self.tela_venda2)
        total_saida.place(x=136, y=360)

        salvar = Button(self.tela_venda2, text="Finalizar", command=self.registra_compra)
        salvar.place(x=200, y=430)
        voltar = Button(self.tela_venda2, text="Voltar", command=self.voltar)
        voltar.place(x=450, y=430)

        self.tela_venda2.mainloop()

    def voltar(self):
        self.tela_venda2.destroy()

    def retorna_data(self):
        data_atual = date.today()
        data = data_atual.strftime('%d/%m/%Y')

        return data

    def registra_compra(self):
        # query = "INSERT INTO `Construct`.`Venda_Materiais` (Cliente)"
        pass


