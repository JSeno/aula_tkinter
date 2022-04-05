""" Importando tkinter"""
from tkinter import * # Importando tkinter * Todos os módulos


janela = Tk() # Criando a janela

# Criando uma instancia do tkinter
janela.title("Button") # Titulo da janela
janela.geometry("250x250") # Tamanho da janela (Largura x Altura) + Posição X + Posição Y

contador = 0 # Criando um botão

def executar(): # Criando uma função

    global contador # Criando uma variavel global

    text_1 = 'Número impar: '
    text_2 = 'Número par: '

    if contador %2 == 0: # Se o contador for par
        resultado = text_2 + str(contador) # Resultado é text_2 + contador
        label_name['text'] = resultado # Label_name é o label_name e o text é o resultado
        label_name['fg'] = '#24851e' # Label_name mudando a cor do texto
    else:
        resultado = text_1 + str(contador) # Resultado é text_2 + contador
        label_name['text'] = resultado # Label_name é o label_name e o text é o resultado
        label_name['fg'] = '#2586c2' # label_name mudando a cor do texto

    contador += 1 # Adicionando 1 ao contador


label_name = Label(janela, width=20, height=2, text='Seu Texto', fg='#f55442', bg='#121211') # Criando um label, tamanho do label, texto do label, fonte do label e propriedasdes do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
label_name.grid(row=0, column=0, padx=5, pady=10) # Posicionando o label na janela, row=linha, column=coluna, pady=padding

button = Button(janela, command=executar, width=8, height=2, text=' Clique Aqui! ', relief='raised', fg='#fcb603', bg='#ffffff') # Criando um botão, tamanho do botão, texto do botão, fonte do botão, propriedades do texto, e cor do texto e cor de fundo, fg=foreground, bg=background
button.grid(row=0, column=1, padx=5, pady=10) # Posicionando o botão na janela, row=linha, column=coluna, pady=padding, padx=padding

janela.mainloop() # Loop infinito, sempre rodando deve ser sempre .mainloop(), as variaveis devem vir antes do .mainloop()


