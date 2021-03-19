from tkinter import *


nome_fornecedor = StringVar
endereco_fornecedor = StringVar
telefone_fornecedor = StringVar


class principal(Frame):

    def __init__(self):
        top = Tk()
        top.title("Fechamento Caixa")
        top.geometry("700x500")
        top.configure(background='#D3D3D3')

        canvas = Canvas(top, width=1366, height=768, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 50, 650, 300, fill="white")
        canvas.place(x=0, y=0)

        nome_fornecedor_label = Label(text="Nome do Fornecedor: ")
        nome_fornecedor_label.place(x=70, y=100)

        nome_fornecedor_label2 = Label(text=nome_fornecedor)
        nome_fornecedor_label2.place(x=220, y=100)


        endereco_fornecedor_label = Label(text="Endereço do Fornecedor: ")
        endereco_fornecedor_label.place(x=70, y=150)

        endereco_fornecedor_label2 = Label(text=endereco_fornecedor)
        endereco_fornecedor_label2.place(x=220, y=150)


        telefone_fornecedor_label = Label(text="Telefone: ")
        telefone_fornecedor_label.place(x=70, y=200)

        telefone_fornecedor_label2 = Label(text=telefone_fornecedor)
        telefone_fornecedor_label2.place(x=320, y=200)

        encerrar_fechamento_caixa = Button(text="Encerrar")  # ,command=Caixa)
        encerrar_fechamento_caixa.place(x=150, y=250)

        desistir_fechamento_caixa = Button(text="Desistir")  # ,command=Caixa)
        desistir_fechamento_caixa.place(x=400, y=250)


        top.mainloop()




