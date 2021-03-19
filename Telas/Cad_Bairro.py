from tkinter import *
import Conexao.ConexaoBd


class CadastroBairro(Frame):

    def __init__(self):
        self.tela_cad_bairro = Tk()
        self.tela_cad_bairro.geometry("600x400")
        self.tela_cad_bairro.title("Cadastrar Bairro")
        self.tela_cad_bairro.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cad_bairro, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_bairro_label = Label(self.tela_cad_bairro, text="Nome do Bairro:")
        nome_bairro_label.place(x=70, y=130)
        self.nome_bairro_entrada = Entry(self.tela_cad_bairro, width=43)
        self.nome_bairro_entrada.place(x=180, y=130)

        salvar = Button(self.tela_cad_bairro, text="Cadastrar", command=self.cadastrar_bairro)
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_cad_bairro, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_cad_bairro.mainloop()

    def voltar(self):
        self.tela_cad_bairro.destroy()

    def cadastrar_bairro(self):
        query = f"INSERT INTO `Construct`.`Bairro` (barNome) VALUES (\"{self.nome_bairro_entrada.get()}\");"
        Conexao.ConexaoBd.cursor.execute(query)

        Conexao.ConexaoBd.conexao.commit()

        self.voltar()


