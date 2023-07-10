#Importações

from tkinter import *
from playsound import playsound
from gtts import *
import os

#Cores

fundo = '#0A0A3F'
letra = '#D3D3EE'
caixa = '#010112'
cor_botao = '#06AFEE'

#Codigo

root = Tk()
root.title("Conversor de texto para audio")
root.geometry('500x420')
root.maxsize(500,420)
root.minsize(500,420)
root.configure(bg=fundo)

#Funções

def margem(altura):
    tela = Canvas(root, width=500, height= altura, bg=fundo , bd= 0, highlightthickness= 0, relief= "ridge")
    tela.pack()
    
def botao(texto, comando, padx):
    botao = Button(root, text=texto,padx=padx, pady=20, command=comando, fg=letra, activeforeground=letra, bg=cor_botao, relief=FLAT, font=("Gotham", 16, 'bold'))
    botao.pack()
    
def comeca():
    texto_inserido = e.get()
    fala = gTTS( text = texto_inserido, lang = 'pt', slow=False, tld='com.br' )
    arquivo_fala = 'arquivo_fala.mp3'
    fala.save(arquivo_fala)
    playsound(arquivo_fala)
    

def resetar():
    e.delete(0, END)
    os.remove('arquivo_fala.mp3')
    
#Textos
margem(20)
titulo = Label(root, bg=fundo, fg= letra, font=("Gotham", 18, 'bold'), text='Conversor de texto para audio')
titulo.pack()

margem(30)
insere_texto = Label(root, bg=fundo, fg= letra, font=("Gotham", 17, ), text='Insira o seu texto:')
insere_texto.pack()

margem(10)
e= Entry(root, width= 25, borderwidth= 4, relief=FLAT, foreground=letra, bg=caixa, font=('Gotham', 21, 'bold'), justify= CENTER)
e.pack()

#Botões
margem(20)
botao_iniciar = botao("COMEÇAR", comeca, 37)

margem(20)
botao_resetar = botao("RESETAR", resetar, 30)
root.mainloop()



