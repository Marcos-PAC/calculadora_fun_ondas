from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import base64

import awesometkinter as atk

#-----------------------------------Paleta de Cores:-----------------------------------
cor1 = '#3b3b3b' # preta / black
cor2 = '#ffffff' # branca / white
cor3 = '#48b3e0' # azul / blue
contador = 0 

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("850x460")
janela.resizable(False, False)
janela.tk.call('wm', 'iconphoto', janela._w, tk.PhotoImage(file='CALCULADORA_TESTE_2/imagens/frequencia2.png'))


#-----------------------------------criando os Frames.-----------------------------------

frame_cima = Frame(janela, width=450, height=50, bg= cor2, padx=3, pady=0, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=510, bg= cor2, padx=3, pady=0, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=400, height=510, bg= cor2, padx=3, pady=0, relief='flat')
frame_direita.place(x=454, y=2)

#-----------------------------------empacotando imagens.-----------------------------------

def images_64():
    pass
#-----------------------------------estilo dos Frames.-----------------------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")
#Imagem 
img = PhotoImage(file="CALCULADORA_TESTE_2/imagens/pngegg.png")
label_image = Label(janela, image=img, borderwidth=0)
label_image.place(x=454,y=370)

img6 = PhotoImage(file="CALCULADORA_TESTE_2/imagens/icone.png")
label_image2 = Label(janela, image=img6, borderwidth=0)
label_image2.place(x=10,y=2)

img7 = PhotoImage(file="CALCULADORA_TESTE_2/imagens/burro.png")
label_image7 = Label(janela, image=img7, borderwidth=0)
label_image7.place(x=460,y=330)

#-----------------------------------Configurando Frame Cima-----------------------------------

l_nome_app = Label(frame_cima, 
                    text= "Calculadora de Funções:",
                    justify= "center",
                    height=1, padx=0,
                    relief='flat',
                    anchor='center',
                    font='ivy 15 bold',
                    bg=cor2, fg= cor3
                    )
l_nome_app.place(x = 50, y = 10)

#-----------------------------------Configurando a funcionalidade do Programa-----------------------------------
def calcular_funcao():
    equacao = 0
    print(equacao)
    print(l_nome_funcao['text'])

    if (l_nome_funcao['text'] == "Frequência:"):

        periodo = float(valor_1.get())
        freq = (1/periodo)
        l_resultado['text'] = (f"A frequência vale: {freq}")
        l_resultado.place(x= 117, y= 240)

    if (l_nome_funcao['text'] == "Interferência Sonora:"):
        
        com_onda = float(valor_2.get())
        d1 = float(valor_3.get())
        d2 = float(valor_4.get())

        valor_n = (2*(d2 -d1))/com_onda

        l_resultado['text'] = (f"O valor de n vale: {valor_n}")
        l_resultado.place(x= 110, y= 340)

    if (l_nome_funcao['text'] == "Velocidade da Onda:"):

        com_onda = float(valor_2.get())
        freq = float(valor_3.get())
        
        velocidade = (com_onda * freq)

        l_resultado['text'] = (f"O valor da velocidade é: {velocidade}")
        l_resultado.place(x= 95, y= 330)


    if (l_nome_funcao['text'] == "Tubos Abertos:"):

        velocidade = float(valor_2.get())
        valor_n = float(valor_3.get())
        d = float(valor_4.get())

        freq = (velocidade*valor_n)/(2*d)
    
        l_resultado['text'] = (f"O valor da frequência é: {freq}")
        l_resultado.place(x= 85, y= 340)

    if (l_nome_funcao['text'] == "Tubos Fechados:"):
    
        velocidade = float(valor_2.get())
        valor_n = float(valor_3.get())
        d = float(valor_4.get())

        freq = (velocidade*valor_n)/(4*d)
    
        l_resultado['text'] = (f"O valor da frequência é: {freq}")
        l_resultado.place(x= 85, y= 340)

    if (l_nome_funcao['text'] == "Intensidade Sonora:"):

        energia = float(valor_2.get())
        valor_area = float(valor_3.get())
        intervalo_temp = float(valor_4.get())

        intensidade = (energia)/(valor_area * intervalo_temp)
    
        l_resultado['text'] = (f"O valor da Intensidade Sonora é: {intensidade}")
        l_resultado.place(x= 45, y= 340)



def restaura_frame():
    #Função restaura o frame a direita possibilitando que novo formulário seja impresso!

    l_variavel.place(x = 980, y = 980)
    valor_1.place(x = 980, y = 980)
    l_variavel2.place(x = 980, y = 980)
    valor_2.place(x = 980, y = 980)
    l_variavel3.place(x = 980, y = 980)
    valor_3.place(x = 980, y = 980)
    l_variavel4.place(x = 980, y = 980)
    valor_4.place(x = 980, y = 980)
    b_calcular.place(x = 980, y = 980)
    b_limpar.place (x = 950, y = 980)
    l_resultado.place(x = 930, y = 920)
    l_explicacao['text'] = ''

def limpa_entry(): 
    #Função restaura o valor nulo das entrys!

    valor_1.delete(0, 'end')
    valor_2.delete(0, 'end')
    valor_3.delete(0, 'end')
    valor_4.delete(0, 'end')
    l_resultado.place(x = 930, y = 920)



def mostrar_frequencia(titulo, nome_valor1, i) ->  tk.Entry:
    #Função apresenta na tela a calculadora respectiva do botão frequência!

    restaura_frame()
    limpa_entry()
    l_variavel.place(x = 30, y = 180)   
    valor_1.place(x = 180, y = 180)
    b_calcular.place (x = 220, y = 280)
    b_limpar.place (x = 100, y = 280)


    l_nome_funcao ['text'] = titulo
    l_variavel['text'] = nome_valor1
    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor do periodo em segundos \n\
     para que a calculadora te retorne a frequência.'


    valor_1 ['width'] = 21


def mostrar_velocidade(titulo, nome_valor1,nome_valor2,i) :
    #Função apresenta na tela a calculadora respectiva do botão Velocidade!

    restaura_frame()
    limpa_entry()
    l_variavel2.place(x = 30, y = 180)
    valor_2.place(x = 128, y = 180)
    l_variavel3.place(x = 30, y = 220)
    valor_3.place(x = 190, y = 220)
    b_calcular.place (x = 220, y = 280)
    b_limpar.place (x = 100, y = 280)
    
    l_nome_funcao['text'] = titulo
    l_variavel2['text'] = nome_valor1
    l_variavel3['text'] = nome_valor2
    valor_3 ['width'] = 20
    valor_2 ['width'] = 27

    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor do comprimento de onda (m): \n\
     Informar o valor da frequência (Hz): \n\
     para que a calculadora te retorne a velocidade desejada.'


def mostrar_interferencia(titulo, nome_valor1,nome_valor2,nome_valor3, i):
    #Função apresenta na tela a calculadora respectiva do botão Interferência!

    restaura_frame()
    limpa_entry()
    l_variavel2.place(x = 30, y = 180)
    valor_2.place(x = 128, y = 180)
    l_variavel3.place(x = 30, y = 220)
    valor_3.place(x = 128, y = 220)
    l_variavel4.place(x = 30, y = 260)
    valor_4.place(x = 128, y = 260)
    b_calcular.place (x = 200, y = 300)
    b_limpar.place (x = 100, y = 300)
    
    l_nome_funcao['text'] = titulo
    l_variavel2['text'] = nome_valor1
    l_variavel3['text'] = nome_valor2
    l_variavel4['text'] = nome_valor3
    valor_3 ['width'] = 27
    valor_2 ['width'] = 27
    valor_4 ['width'] = 27

    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor do comprimento de onda (m): \n\
     Informar o valor de d1 (m): \n\
     Informar o valor de d2 (m): \n\
     para que a calculadora te retorne o n desejado.'



def mostrar_tubos_abertos(titulo, nome_valor1,nome_valor2, nome_valor3,i):
    #Função apresenta na tela a calculadora respectiva do botão tubos abertos! 
    
    restaura_frame()
    limpa_entry()
    l_variavel2.place(x = 30, y = 180)
    valor_2.place(x = 200, y = 180)
    l_variavel3.place(x = 30, y = 220)
    valor_3.place(x = 128, y = 220)
    l_variavel4.place(x = 30, y = 260)
    valor_4.place(x = 128, y = 260)
    b_calcular.place (x = 200, y = 300)
    b_limpar.place (x = 100, y = 300)
    
    
    l_nome_funcao['text'] = titulo
    l_variavel2['text'] = nome_valor1
    l_variavel3['text'] = nome_valor2
    l_variavel4['text'] = nome_valor3
    valor_2 ['width'] = 19
    valor_3 ['width'] = 27
    valor_4 ['width'] = 27
    
    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor da velocidade (m/s): \n\
     Informar o valor de n: \n\
     Informar o valor de  d (m): \n\
     para que a calculadora te retorne a frequência desejado.'
    

def mostrar_tubos_fechados(titulo, nome_valor1,nome_valor2, nome_valor3,i): 
    #Função apresenta na tela a calculadora respectiva do botão tubos abertos! 
    
    restaura_frame()
    limpa_entry()
    l_variavel2.place(x = 30, y = 180)
    valor_2.place(x = 200, y = 180)
    l_variavel3.place(x = 30, y = 220)
    valor_3.place(x = 128, y = 220)
    l_variavel4.place(x = 30, y = 260)
    valor_4.place(x = 128, y = 260)
    b_calcular.place (x = 200, y = 300)
    b_limpar.place (x = 100, y = 300)
    

    l_nome_funcao['text'] = titulo
    l_variavel2['text'] = nome_valor1
    l_variavel3['text'] = nome_valor2
    l_variavel4['text'] = nome_valor3
    valor_2 ['width'] = 19
    valor_3 ['width'] = 27
    valor_4 ['width'] = 27
    
    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor da velocidade (m/s): \n\
     Informar o valor de n: \n\
     Informar o valor de  d (m): \n\
     para que a calculadora te retorne a frequência desejado.'

def mostrar_intensidade(titulo, nome_valor1,nome_valor2,nome_valor3, i):
    #Função apresenta na tela a calculadora respectiva do botão Interferência!

    restaura_frame()
    limpa_entry()
    l_variavel2.place(x = 30, y = 180)
    valor_2.place(x = 175, y = 180)
    l_variavel3.place(x = 30, y = 220)
    valor_3.place(x = 155, y = 220)
    l_variavel4.place(x = 30, y = 260)
    valor_4.place(x = 192, y = 260)
    b_calcular.place (x = 200, y = 300)
    b_limpar.place (x = 100, y = 300)
    
    l_nome_funcao['text'] = titulo
    l_variavel2['text'] = nome_valor1
    l_variavel3['text'] = nome_valor2
    l_variavel4['text'] = nome_valor3
    valor_3 ['width'] = 24
    valor_2 ['width'] = 22
    valor_4 ['width'] = 20

    l_explicacao['text'] = '     Para essa funcionalidade é importante saber:\n \
    Informar o valor da Energia (J): \n\
     Informar o valor da Área (m^2): \n\
     Informar o valor do intervalo de tempo (s): \n\
     para que a calculadora te retorne a intensidade desejada.'

    


#-----------------------------------Configurando Frame Esquerda-----------------------------------


#Botão de Frequência:

img_0 = Image.open("CALCULADORA_TESTE_2/imagens/frequencia3.png")
img_0 = img_0.resize((50,50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

b_0 = Button(frame_esquerda, 
                    text= "Frequência",
                    image = img_0, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 11 ',
                    bg=cor3, fg= cor2,
                    command= (lambda:mostrar_frequencia('Frequência:','Valor do Periodo:', 1))
                    )
b_0.grid(row=0, columnspan=4, sticky=NSEW, padx=5, pady=5)

#Botão de Velocidade da Onda:
img_1 = Image.open('CALCULADORA_TESTE_2/imagens/plot2.png')
img_1 = img_1.resize((45,45), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)

b_1 = Button(frame_esquerda, 
                    text= "Velocidade da Onda ",
                    image = img_1, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 11 ',
                    bg=cor3, fg= cor2,
                    command= lambda:mostrar_velocidade('Velocidade da Onda:', "Valor de λ:", "Valor da frequência:",3)
                
                    )
b_1.grid(row=2, columnspan=4, sticky=NSEW, padx=5, pady=5)

#Botão de Interferência:

img_2 = Image.open('CALCULADORA_TESTE_2/imagens/dif_caminhos2.png')
img_2 = img_2.resize((50,50), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)

b_2 = Button(frame_esquerda, 
                    text= "Interferência Sonora",
                    image = img_2, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 11 ',
                    bg=cor3, fg= cor2,
                    command= lambda:mostrar_interferencia('Interferência Sonora:', "Valor de λ:", "Valor de d1:", "Valor de d2:",2)
                    
                    )
b_2.grid(row=1, columnspan=4, sticky=NSEW, padx=5, pady=5)

#Botão de Interferência:

img_5 = Image.open('CALCULADORA_TESTE_2/imagens/Intensidade.png')
img_5 = img_5.resize((50,50), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)

b_5 = Button(frame_esquerda, 
                    text= "Intensidade Sonora",
                    image = img_5, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 11 ',
                    bg=cor3, fg= cor2,
                    command= lambda:mostrar_intensidade('Intensidade Sonora:', "Valor da Energia:", "Valor da Área:", "Intervalo de tempo:",2)
                    
                    )
b_5.grid(row=3, columnspan=4, sticky=NSEW, padx=5, pady=5)

#Botão de Frêquência de Ondas Estacionárias: Tubos Abertos:

img_3 = Image.open('CALCULADORA_TESTE_2/imagens/docaina4.png')
img_3 = img_3.resize((45,45), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)

b_3 = Button(frame_esquerda, 
                    text= "Frêquência de Ondas Estacionárias: Tubos Abertos",
                    image = img_3, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 10 bold',
                    bg=cor3, fg= cor2,
                    command= lambda:mostrar_tubos_abertos('Tubos Abertos:', 'Valor da Velocidade:', 'Valor de n:', 'Valor de d:',4)
                   
                    )
b_3.grid(row=4, columnspan=4, sticky=NSEW, padx=5, pady=5)

#Botão de Frêquência de Ondas Estacionárias: Tubos fechados:

img_4 = Image.open('CALCULADORA_TESTE_2/imagens/pan3.png')
img_4 = img_4.resize((45,45), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)

b_4 = Button(frame_esquerda, 
                    text= "Frêquência de Ondas Estacionárias: Tubos Fechados",
                    image = img_4, compound= LEFT,
                    height=50, width=450,
                    relief='flat', overrelief='solid', 
                    anchor='nw',
                    font='ivy 10 bold',
                    bg=cor3, fg= cor2,
                    command= lambda:mostrar_tubos_fechados('Tubos Fechados:', 'Valor da Velocidade:', 'Valor de n:', 'Valor de d:',5)
                    
                    )
b_4.grid(row=5, columnspan=4, sticky=NSEW, padx=5, pady=5)

#-----------------------------------Configurando Frame direita-----------------------------------

l_nome_funcao = Label(frame_direita, 
                    text= "Função",
                    height=2, width=35, padx=0,
                    relief='groove',
                    anchor='center',
                    font='ivy 15 bold',
                    bg=cor2, fg= cor1
                    )
l_nome_funcao.place(x = -5, y = -2)

# Explicação Física da Bagaça:

l_explicacao = Label(frame_direita, 
                    text= "",
                    height=6, width=49, padx=0, pady=0,
                    justify= LEFT,
                    relief='groove',
                    anchor='w',
                    font='ivy 10 bold',
                    bg=cor2, fg= cor1
                    )
l_explicacao.place(x = -3, y = 50)

# calculadora:

l_variavel = Label(frame_direita, 
                    text= "",
                   justify= "center",
                    height=1, padx=0,
                    relief='flat',
                    anchor='center',
                    font='ivy 12 bold',
                    bg=cor2, fg= cor3
                    )
l_variavel.place(x = 960, y = 980)
valor_1 = tk.Entry(frame_direita, borderwidth=2, width=20, font="Ivy 12 bold")
valor_1.place(x = 980, y = 980)

l_variavel2 = Label(frame_direita, 
                    text= "",
                    justify= "center",
                    height=1, padx=0,
                    relief='flat',
                    anchor='center',
                    font='ivy 12 bold',
                    bg=cor2, fg= cor3
                    )
l_variavel2.place(x = 900, y = 980)

valor_2 = tk.Entry(frame_direita, borderwidth=2, width=27, font="Ivy 12 bold")
valor_2.place(x = 928, y = 980)

l_variavel3 = Label(frame_direita, 
                    text= "",
                    justify= "center",
                    height=1, padx=0,
                    relief='flat',
                    anchor='center',
                    font='ivy 12 bold',
                    bg=cor2, fg= cor3
                    )
l_variavel3.place(x = 930, y = 920)

valor_3 = tk.Entry(frame_direita, borderwidth=2, width=20, font="Ivy 12 bold")
valor_3.place(x = 990, y = 920)

l_variavel4 = Label(frame_direita, 
                    text= "",
                    justify= "center",
                    height=1, padx=0,
                    relief='flat',
                    anchor='center',
                    font='ivy 12 bold',
                    bg=cor2, fg= cor3
                    )
l_variavel4.place(x = 930, y = 920)

valor_4 = tk.Entry(frame_direita, borderwidth=2, width=20, font="Ivy 12 bold")
valor_4.place(x = 990, y = 920)

b_calcular = Button(frame_direita, 
                    text= "Calcular",
                    height=1, width=9,
                    relief='flat', overrelief='solid', 
                    font='ivy 10 bold',
                    bg=cor3, fg= cor2,
                    command= lambda:calcular_funcao()
                    )
b_calcular.place (x = 950, y = 980)

b_limpar = Button(frame_direita, 
                    text= "Limpar",
                    height=1, width=9,
                    relief='flat', overrelief='solid', 
                    font='ivy 10 bold',
                    bg=cor3, fg= cor2,
                    command= lambda:limpa_entry()
                    )
b_limpar.place (x = 950, y = 980)

l_resultado = Label(frame_direita, 
                    text= "",
                    justify= "center",
                    height=1, padx=0,
                    relief='groove',
                    anchor='center',
                    font='ivy 12 bold',
                    bg=cor2, fg= cor3
                    )
l_resultado.place(x = 930, y = 920)


janela.mainloop()
