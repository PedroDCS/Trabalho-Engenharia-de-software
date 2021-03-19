from tkinter import *
from tkinter import ttk

valor = DoubleVar
nome_produto_bd = StringVar
codigo_produto_bd = 0
total_estoque_produto_bd = float
estoque_minimo_produto_bd = float
preco_compra_produto_bd = "12"
preco_venda_produto_bd = float

class Estoque(Frame):

    def __init__(self):
        tela_estoque = Tk()
        tela_estoque.title("Estoque")
        tela_estoque.geometry("600x450")
        tela_estoque.configure(background='#ccd7ff')

        canvas = Canvas(tela_estoque, width=900, height=500, background='#ccd7ff')

        r1 = canvas.create_rectangle(50, 50, 550, 400, fill="white", outline='red', width=3)
        canvas.place(x=0, y=0)

        codigo_produto_label = ttk.Combobox(tela_estoque, width=17, font='Bahnschrift',
                                     values=["1",
                                             "2",
                                             "3",
                                             "4"])
        codigo_produto_label.place(x=70, y=60)



        # codigo_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift', bd=0, text="Codigo do Produto: ")
        # codigo_produto_label.place(x=70, y=60)
        #
        codigo_produto = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift', bd=0, text=codigo_produto_bd)
        codigo_produto.place(x=250, y=60)


        nome_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Nome do Produto: ")
        nome_produto_label.place(x=70, y=100)

        nome_produto = Label(tela_estoque, bg="#cad8f4", width=30, activebackground='white', font='Bahnschrift',  bd=0, text=nome_produto_bd)
        nome_produto.place(x=230, y=100)



        total_estoque_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Total em Estoque: ")
        total_estoque_produto_label.place(x=70, y=150)

        total_estoque_produto = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text=total_estoque_produto_bd)
        total_estoque_produto.place(x=220, y=150)


        estoque_minimo_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Estoque Minimo: ")
        estoque_minimo_produto_label.place(x=70, y=200)

        estoque_minimo_produto = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text=estoque_minimo_produto_bd)
        estoque_minimo_produto.place(x=220, y=200)


        proco_compra_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Preço de Compra R$: ")
        proco_compra_produto_label.place(x=70, y=250)

        proco_compra_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text=preco_compra_produto_bd)
        proco_compra_produto_label.place(x=220, y=250)


        proco_venda_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="Preço de Venda R$: ")
        proco_venda_produto_label.place(x=70, y=300)

        proco_venda_produto_label = Label(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text=preco_venda_produto_bd)
        proco_venda_produto_label.place(x=220, y=300)

        salvar_tela_estoque = Button(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="SALVAR")  # ,command=Caixa)
        salvar_tela_estoque.place(x=70, y=350)

        fechar_tela_estoque = Button(tela_estoque, bg="#cad8f4", width=17, activebackground='white', font='Bahnschrift',  bd=0, text="FECHAR")  # ,command=Caixa)
        fechar_tela_estoque.place(x=300, y=350)

        tela_estoque.mainloop()

    def ChamaCodigo(self):
        codigo_produto_bd = codigo_produto_label