''' GRID TKINTER 

row 0    | row 0    | row 0
column 0 | column 1 | column 2
______________________________
row 1    | row 1    | row 1
column 0 | column 1 | column 2
______________________________
row 2    | row 2    | row 2
column 0 | column 1 | column 2

'''
# Entry


# Importando Tkinter * Todos os módulos
from tkinter import *

# Criando uma instancia do tkinter
janela = Tk() # Criando a janela
janela.title('Entry') # Titulo da janela
janela.geometry('400x350') # Tamanho da janela (Largura x Altura) + Posição X + Posição Y


''' Função entrada de dados '''
def obter():
    nome = entry_nome.get() # Pegando o que foi digitado no Entry
    idade = entry_idade.get() # Pegando o que foi digitado no Entry
    pais = entry_pais.get() # Pegando o que foi digitado no Entry

    # Aqui é onde vai aparecer o que foi digitado no Entry
    label_name_re['text'] = nome.capitalize() # Atribuindo o que foi digitado no Entry ao Label
    label_idade_re['text'] = idade # Atribuindo o que foi digitado no Entry ao Label
    label_pais_re['text'] = pais.capitalize() # Atribuindo o que foi digitado no Entry ao Label

    # Limpando o Entry
    entry_nome.delete(0, END) # Limpando os dados digitados no Entry
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)



''' Nome '''
label_name = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 10'), anchor='w') # Criando um label, tamanho do label, texto do label, fonte do label e propriedasdes do texto, e cor do texto e cor de fundo, fg=foreground, bg=background, anchor=Centraliza o texto na linha
label_name.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW) # Posicionando o label na janela, row=linha, column=coluna, pady=y padding, sticky=sticky, N=North, S=South, E=East, W=West
entry_nome = Entry(janela, width=10, font=('Arial 10 ')) # Criando uma entrada de dados com largura e o tamanho é definido pela font do texto
entry_nome.grid(row=0, column=1, padx=5, pady=5) # grid(row=linha, column=coluna, pady=y padding, padx=x padding)

''' Idade '''
label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 10'), anchor='w') 
label_idade.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW) 
entry_idade = Entry(janela, width=10, font=('Arial 10 '))
entry_idade.grid(row=1, column=1, padx=5, pady=5)

'''País '''
label_pais = Label(janela, width=10, height=2, text='País: ', font=('Arial 10'), anchor='w') 
label_pais.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
entry_pais = Entry(janela, width=10, font=('Arial 10 '), state=DISABLED) # state é o estado do Entry, DISABLED=desabilitado
entry_pais.grid(row=2, column=1, padx=5, pady=5)

''' Resposta '''
label_name_re = Label(janela, width=20, height=2, text=' ', font=('Arial 10'), anchor='w')
label_name_re.grid(row=0, column=2, padx=20, pady=5, sticky=NSEW)

label_idade_re = Label(janela, width=20, height=2, text=' ', font=('Arial 10'), anchor='w')
label_idade_re.grid(row=1, column=2, padx=20, pady=5, sticky=NSEW)

label_pais_re = Label(janela, width=20, height=2, text=' ', font=('Arial 10'), anchor='w')
label_pais_re.grid(row=2, column=2, padx=20, pady=5, sticky=NSEW)

#  Esse botão vai obter os dados digitados e exibir na tela onde
button = Button(janela, command=obter, width=20, height=2, text='Mostrar dados', relief='raised', fg='#fcb603', bg='#ffffff') # Criando um botão, tamanho do botão, texto do botão, fonte do botão, propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
button.grid(row=3, column=2, padx=5, pady=20) # Posicionando o botão na janela, row=linha, column=coluna, pady=padding, padx=padding

janela.mainloop() # Loop infinito, sempre rodando deve ser sempre .mainloop(), as variaveis devem vir antes do .mainloop()