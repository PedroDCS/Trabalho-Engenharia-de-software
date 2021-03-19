from tkinter import *

valor = DoubleVar
nome_produto_bd = StringVar
codigo_produto_bd = 0
total_estoque_produto_bd = float
estoque_minimo_produto_bd = float
preco_compra_produto_bd = "12"
preco_venda_produto_bd = float




class CadastroMercadoria(Frame):

    def __init__(self):
        self.tela_cadastro_mercadoria = Tk()
        self.tela_cadastro_mercadoria.title("Cadastro Mercadoria")
        self.tela_cadastro_mercadoria.geometry("600x500")
        self.tela_cadastro_mercadoria.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cadastro_mercadoria, width=800, height=600, background='#ccd7ff')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 400, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)
        
        
        codigo_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift', bd=0, text="Codigo do Produto: ")
        codigo_produto_label.place(x=70, y=60)

        codigo_produto = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17, font='Bahnschrift', bd=0, text=codigo_produto_bd)
        codigo_produto.place(x=250, y=60)

        nome_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text="Nome do Produto: ")
        nome_produto_label.place(x=70, y=100)

        nome_produto = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=30,  font='Bahnschrift',  bd=0, text=nome_produto_bd)
        nome_produto.place(x=245, y=100)

        total_estoque_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text="Total em Estoque: ")
        total_estoque_produto_label.place(x=70, y=150)

        total_estoque_produto = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text=total_estoque_produto_bd)
        total_estoque_produto.place(x=230, y=150)

        estoque_minimo_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text="Estoque Minimo: ")
        estoque_minimo_produto_label.place(x=70, y=200)

        estoque_minimo_produto = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text=estoque_minimo_produto_bd)
        estoque_minimo_produto.place(x=230, y=200)

        proco_compra_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=18,  font='Bahnschrift',  bd=0, text="Preço de Compra R$: ")
        proco_compra_produto_label.place(x=70, y=250)

        proco_compra_produto_label = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text=preco_compra_produto_bd)
        proco_compra_produto_label.place(x=250, y=250)

        proco_venda_produto_label = Label(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text="Preço de Venda R$: ")
        proco_venda_produto_label.place(x=70, y=300)

        proco_venda_produto_label = Entry(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17,  font='Bahnschrift',  bd=0, text=preco_venda_produto_bd)
        proco_venda_produto_label.place(x=220, y=300)

        salvar = Button(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Salvar")  # ,command=Caixa)
        salvar.place(x=100, y=350)

        voltar = Button(self.tela_cadastro_mercadoria, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Voltar", command=self.voltar)
        voltar.place(x=350, y=350)

        self.tela_cadastro_mercadoria.mainloop()

    def voltar(self):
        self.tela_cadastro_mercadoria.destroy()