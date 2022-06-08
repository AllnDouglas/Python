from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import re 

root = Tk()
root.title("Formulario de contato")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
padraoEmail='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

#==================================FUNÇÕES============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `formulario` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, cpf TEXT, email TEXT, telefone TEXT, mensagem TEXT)")
    
def Enviar():
    if  NOME.get() == "" or CPF.get() == "" or EMAIL.get() == "" or TELEFONE.get() == "" or MENSAGEM.get() == "":
        txt_mensagem.config(text="Por favor, Preencha todos os campos !", fg="red")

    elif len(CPF.get()) != 11 or CPF.get() == CPF.get()[::-1]:
         txt_mensagem.config(text="Cpf invalido !, O cpf deve ter 11 digitos e não deve se colocar pontos ou traços", fg="red")

    elif re.search(padraoEmail,EMAIL.get()):
        txt_mensagem.config(text="Digite um email valido !", fg="red")

    elif len(TELEFONE.get()) < 8 or len(TELEFONE.get()) > 13:
        txt_mensagem.config(text="Digite um telefone valido, pode ser fixo ou celular !", fg="red")

    else:
        Database()
        cursor.execute("INSERT INTO `formulario` (nome, cpf, email, telefone, mensagem) VALUES(?, ?, ?, ?, ?)", (str(NOME.get()), str(CPF.get()), str(EMAIL.get()), str(TELEFONE.get()), str(MENSAGEM.get())))
        conn.commit()
        NOME.set("")
        CPF.set("")
        EMAIL.set("")
        TELEFONE.set("")
        MENSAGEM.set("")
        cursor.close()
        conn.close()
        txt_mensagem.config(text="Dados enviados com sucesso !", fg="green")

def LerDados():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM formulario")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4],data[5]))
    cursor.close()
    conn.close()
    txt_mensagem.config(text="Leitura de dados concluida ! ", fg="black")


def Atualizar():
    Database()
    if len(MENSAGEM.get()) < 100 :
        txt_mensagem.config(text="Por favor, sua mensagem deve ter no minimo 100 letras", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute("UPDATE `formulario` SET `nome` = ?, `cpf` = ?, `email` =?,  `telefone` = ?,  `mensagem` = ? WHERE `id` = ?", (str(NOME.get()), str(CPF.get()), str(EMAIL.get()), str(TELEFONE.get()), str(MENSAGEM.get()), int(id)))
        conn.commit()
        cursor.execute("SELECT * FROM `formulario` ORDER BY `nome` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
        cursor.close()
        conn.close()
        NOME.set("")
        CPF.set("")
        EMAIL.set("")
        TELEFONE.set("")
        MENSAGEM.set("")
        btn_enviar.config(state=NORMAL)
        btn_ler.config(state=NORMAL)
        btn_atualizar.config(state=DISABLED)
        btn_excluir.config(state=NORMAL)
        txt_mensagem.config(text="Dados atualizados com sucesso ! ", fg="black")


def Selecionar(event):
    global id;
    ItemAtual = tree.focus()
    conteudo =(tree.item(ItemAtual))
    itemSelecionado = conteudo['values']
    id = itemSelecionado[0]
    NOME.set("")
    CPF.set("")
    EMAIL.set("")
    TELEFONE.set("")
    MENSAGEM.set("")
    NOME.set(itemSelecionado[1])
    CPF.set(itemSelecionado[2])
    EMAIL.set(itemSelecionado[3])
    TELEFONE.set(itemSelecionado[4])
    MENSAGEM.set(itemSelecionado[5])
    btn_enviar.config(state=DISABLED)
    btn_ler.config(state=DISABLED)
    btn_atualizar.config(state=NORMAL)
    btn_excluir.config(state=DISABLED)

def Excluir():
    if not tree.selection():
       txt_mensagem.config(text="Por favor, selecione um item primeiro", fg="red")
    else:
        resultado = tkMessageBox.askquestion('Formulario de contato', 'Tem certeza que deseja deletar ?', icon="warning")
        if resultado == 'yes':
            ItemAtual = tree.focus()
            conteudo =(tree.item(ItemAtual))
            itemSelecionado = conteudo['values']
            tree.delete(ItemAtual)
            Database()
            cursor.execute("DELETE FROM `formulario` WHERE `id` = %d" % itemSelecionado[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_mensagem.config(text="Dados deletados com sucesso ", fg="black")
            
    
def Sair():
    resultado = tkMessageBox.askquestion('Form de contato', 'Tem certeza que deseja sair ?', icon="warning")
    if resultado == 'yes':
        root.destroy()
        Sair()

#==================================VARIABLES==========================================
NOME = StringVar()
CPF = StringVar()
EMAIL = StringVar()
TELEFONE = StringVar()
MENSAGEM = StringVar()

#==================================FRAMES==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise",bg="#1D3461")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450,bg="#1D3461")
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)



#==================================TEXTOS=======================================
txt_title = Label(Top, width=900, font=('Papyrus', 24), text = "Formulario de contato",bg='#1F4377')
txt_title.pack()
txt_nome = Label(Forms, text="Nome:", font=('Papyrus', 16), bd=15,bg="#1D3461",fg="white")
txt_nome.grid(row=0, stick="e")
txt_cpf = Label(Forms, text="Cpf:", font=('Papyrus', 16), bd=15,bg="#1D3461",fg="white")
txt_cpf.grid(row=1, stick="e")
txt_email = Label(Forms, text="Email:", font=('Papyrus', 16), bd=15,bg="#1D3461",fg="white")
txt_email.grid(row=2, stick="e")
txt_telefone = Label(Forms, text="Telefone:", font=('Papyrus', 16), bd=15,bg="#1D3461",fg="white")
txt_telefone.grid(row=3, stick="e")
txt_mensagem = Label(Forms, text="Mensagem:", font=('Papyrus', 16), bd=15,bg="#1D3461",fg="white")
txt_mensagem.grid(row=4, stick="e")

txt_mensagem = Label(Buttons)
txt_mensagem.pack(side=TOP)

#==================================ENTRADA DE DADOS=======================================
nome = Entry(Forms, textvariable=NOME, width=30,bg='#ccc')
nome.grid(row=0, column=1)
cpf = Entry(Forms, textvariable=CPF, width=30,bg='#ccc')
cpf.grid(row=1, column=1)
email = Entry(Forms, textvariable=EMAIL, width=30,bg='#ccc')
email.grid(row=2, column=1)
telefone = Entry(Forms, textvariable=TELEFONE, width=30,bg='#ccc')
telefone.grid(row=3, column=1)
mensagem = Entry(Forms, textvariable=MENSAGEM, width=30,bg='#ccc')
mensagem.grid(row=4, column=1)

#==================================BOTÕES=====================================
btn_enviar = Button(Buttons, width=10, text="Enviar",bg="#20614A",fg="white", command=Enviar)
btn_enviar.pack(side=LEFT)
btn_ler = Button(Buttons, width=10, text="Ler dados",bg="#9A800E",fg="black", command=LerDados )
btn_ler.pack(side=LEFT)
btn_atualizar = Button(Buttons, width=10, text="Atualizar",bg="#1F487E",fg="white", command=Atualizar)
btn_atualizar.pack(side=LEFT)
btn_excluir = Button(Buttons, width=10, text="Excluir",bg="#EA333C",fg="white",command=Excluir)
btn_excluir.pack(side=LEFT)
btn_sair = Button(Buttons, width=10, text="Sair", command=Sair, bg="black",fg="white")
btn_sair.pack(side=LEFT)

#==================================LISTA DE WIDGETS========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ID" , "NOME", "CPF", "EMAIL", "TELEFONE", "MENSAGEM"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('NOME', text="NOME", anchor=W)
tree.heading('CPF', text="CPF", anchor=W)
tree.heading('EMAIL', text="EMAIL", anchor=W)
tree.heading('TELEFONE', text="TELEFONE", anchor=W)
tree.heading('MENSAGEM', text="MENSAGEM", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', Selecionar)


#==================================EXECUTANDO O PROGRAMA=====================================
if __name__ == '__main__':
    root.mainloop()
