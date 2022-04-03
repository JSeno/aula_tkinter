""" Importando tkinter"""
from tkinter import * # Importando tkinter * Todos os módulos


# Definindo paleta de cores do app com variaveis
cor1 = '#000000'


janela = Tk() # Criando a janela

# Criando uma instancia do tkinter
janela.title("Janela Tkinter") # Titulo da janela

janela.geometry("600x250+200+200") # Tamanho da janela (Largura x Altura) + Posição X + Posição Y

janela.config(bg=cor1) # Cor de fundo da janela, pode usar hexadecimal, rgb, etc

janela.iconphoto(False, PhotoImage(file="icon_clock.png")) # Adicionando icone na janela, False para não redimensionar, PhotoImage(file='caminho do arquivo')

janela.resizable(width=False, height=False) # Não redimensionar a janela, False para não redimensionar


janela.mainloop() # Loop infinito, sempre rodando deve ser sempre .mainloop(), as variaveis devem vir antes do .mainloop()


