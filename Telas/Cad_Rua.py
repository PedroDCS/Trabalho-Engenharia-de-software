from tkinter import *
from tkinter import ttk
import Conexao.ConexaoBd


class CadastroRua(Frame):

    def __init__(self):
        self.tela_cad_rua = Tk()
        self.tela_cad_rua.geometry("600x400")
        self.tela_cad_rua.title("Cadastrar Rua")
        self.tela_cad_rua.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cad_rua, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_rua_label = Label(self.tela_cad_rua, text="Nome da Rua:")
        nome_rua_label.place(x=70, y=100)
        self.nome_rua_entrada = Entry(self.tela_cad_rua, width=43)
        self.nome_rua_entrada.place(x=170, y=100)

        nome_bairro_label = Label(self.tela_cad_rua, text="Bairro:")
        nome_bairro_label.place(x=70, y=160)
        self.combo_bairros = ttk.Combobox(self.tela_cad_rua, values=Conexao.ConexaoBd.listar("SELECT barNome FROM Bairro;"))
        self.combo_bairros.place(x=120, y=160)

        salvar = Button(self.tela_cad_rua, text="Cadastrar", command=self.cadastrar_rua)
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_cad_rua, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_cad_rua.mainloop()

    def voltar(self):
        self.tela_cad_rua.destroy()

    def cadastrar_rua(self):
        codigo_bairro = 0

        query = f"SELECT barCodigo FROM `Construct`.`Bairro` WHERE barNome=\"{self.combo_bairros.get()}\";"
        Conexao.ConexaoBd.cursor.execute(query)

        for c in Conexao.ConexaoBd.cursor:
            codigo_bairro = c[0]

        query = f"INSERT INTO `Construct`.`Rua` (ruaNome, rua_barCodigo) VALUES (\"{self.nome_rua_entrada.get()}\", \"{codigo_bairro}\");"
        Conexao.ConexaoBd.cursor.execute(query)

        Conexao.ConexaoBd.conexao.commit()

        self.voltar()
