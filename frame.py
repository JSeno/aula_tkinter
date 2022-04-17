"""Importando Tkinter * Todos os módulos"""
from tkinter import *

# Criando uma instancia do tkinter
janela = Tk() # Criando a janela

# Definindo o Titulo da janela e o tamanho da janela
janela.title('Frame')
janela.geometry('400x400')

# Criando um frame
frame_nav = Frame(janela, width=400, height=40, bg='white') # Criando um frame, largura, altura e cor de fundo
frame_nav.grid(row=0, column=0, columnspan=3, pady=0, padx=0) # Posicionando o frame na janela, row=linha, column=coluna, columnspan=colunas que ocupa, pady=y padding, padx=x padding

frame_left = Frame(janela, width=100, height=300, bg='blue') # Criando um frame, largura, altura e cor de fundo
frame_left.grid(row=1, column=0, pady=2, padx=2) # Posicionando o frame na janela, row=linha, column=coluna

frame_center = Frame(janela, width=200, height=300, bg='white') # Criando um frame, largura, altura e cor de fundo
frame_center.grid(row=1, column=1, pady=2, padx=2) # Posicionando o frame na janela, row=linha, column=coluna

frame_right = Frame(janela, width=100, height=300, bg='blue') # Criando um frame, largura, altura e cor de fundo
frame_right.grid(row=1, column=2, pady=2, padx=2) # Posicionando o frame na janela, row=linha, column=coluna


# Definindo o Mainloop, ele serve para que a janela não seja fechada
# sempre que o programa for finalizado
janela.mainloop()
