""" Importando Tkinter * Todos os módulos """
from platform import java_ver
from tkinter import *

# Criando uma instancia do tkinter
janela = Tk() # Criando a janela

# Titulo da janela
janela.title('Primeiro Botão Rádio')
# Geometry que é o tamanho da janela (Largura x Altura) + Posição X + Posição Y
janela.geometry('400x350')

# Criando uma função de obtenção de dados
def obter():
    resultado = selecionado_1.get() # Pegando o que foi selecionado no RadioButton
    print(resultado) # Imprimindo o que foi selecionado no RadioButton


# Criando uma variável que vai armazenar o valor do RadioButton
selecionado_1 = IntVar()
selecionado_2 = BooleanVar()
selecionado_3 = StringVar()

# Limpando o RadioButton
selecionado_1.set(0)
selecionado_2.set(False)
selecionado_3.set('')

# Criando um botão radio
radio_1 = Radiobutton(janela, command=obter, text='Primeiro', value=1, variable=selecionado_1) # Criando um botão radio, texto do botão, valor do botão, e o estado do botão
radio_1.grid(row=0, column=0, padx=10, pady=10) # Posicionando o botão radio na janela, row=linha, column=coluna

radio_2 = Radiobutton(janela,command=obter, text='Segundo', value=2, variable=selecionado_2) # Criando um botão radio, texto do botão, valor do botão, e o estado do botão
radio_2.grid(row=1, column=0, padx=10, pady=10) # Posicionando o botão radio na janela, row=linha, column=coluna

radio_3 = Radiobutton(janela,command=obter, text='Terceiro', value=3, variable=selecionado_3) # Criando um botão radio, texto do botão, valor do botão, e o estado do botão
radio_3.grid(row=2, column=0, padx=10, pady=10) # Posicionando o botão radio na janela, row=linha, column=coluna






# Mainloop que é o loop principal deve ser sempre a última linha do código
# para que o programa não seja fechado
janela.mainloop()