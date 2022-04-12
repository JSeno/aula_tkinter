""" Importando tkinter"""
from tkinter import * # Importando tkinter * Todos os módulos


janela = Tk() # Criando a janela

# Criando uma instancia do tkinter
janela.title("Grid") # Titulo da janela

janela.geometry("300x300") # Tamanho da janela (Largura x Altura) + Posição X + Posição Y

label_name = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15 bold'), fg='#f55442', bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedasdes do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_name.grid(row=0, column=0) # row=linha, column=coluna, pady=padding
name = Label(janela, width=10, height=2, text='Jefferson', font=('Arial 15 bold'), fg='#f55442', bg='#6298f5') # Criando um label, tamanho do label, texto do label, fonte do label e propriedasdes do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
name.grid(row=0, column=1) # row=linha, column=coluna, pady=padding

label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold'), fg='#f5aa42', bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_idade.grid(row=1, column=0) # row=linha, column=coluna, pady=padding
idade = Label(janela, width=10, height=2, text='22', font=('Arial 15 bold'), fg='#f5aa42', bg='#6298f5') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
idade.grid(row=1, column=1) # row=linha, column=coluna, pady=padding

label_pais = Label(janela, width=10, height=2, text='País: ', font=('Arial 15 bold'), fg='#acc938',  bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_pais.grid(row=2, column=0) # row=linha, column=coluna, pady=padding
pais = Label(janela, width=10, height=2, text='HueBr', font=('Arial 15 bold'), fg='#acc938',  bg='#6298f5') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
pais.grid(row=2, column=1) # row=linha, column=coluna, pady=padding

janela.mainloop() # Loop infinito, sempre rodando deve ser sempre .mainloop(), as variaveis devem vir antes do .mainloop()


