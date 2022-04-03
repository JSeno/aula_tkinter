""" Importando tkinter"""
from tkinter import * # Importando tkinter * Todos os módulos


janela = Tk() # Criando a janela

# Criando uma instancia do tkinter
janela.title("Label") # Titulo da janela

janela.geometry("250x250+200+200") # Tamanho da janela (Largura x Altura) + Posição X + Posição Y

label_name = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15 bold'), fg='#f55442', bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedasdes do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_name.grid(row=0, column=0, pady=10) # Posicionando o label na janela, row=linha, column=coluna, pady=padding

label_name = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold'), fg='#f5aa42', bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_name.grid(row=1, column=0, pady=10) # Posicionando o label na janela, row=linha, column=coluna, pady=padding

label_name = Label(janela, width=10, height=2, text='País: ', font=('Arial 15 bold'), fg='#acc938',  bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_name.grid(row=2, column=0, pady=10) # Posicionando o label na janela, row=linha, column=coluna, pady=padding

janela.mainloop() # Loop infinito, sempre rodando deve ser sempre .mainloop(), as variaveis devem vir antes do .mainloop()


