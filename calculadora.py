#importando biblioteca para utilizar Widget
from tkinter import *
from tkinter import ttk
from turtle import goto, right

#Definindo as cores

cor1 = "#0e1414" #preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

#Criando "janelas".
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
#Alterar background
janela.config(bg=cor1)

#Criando frames para separar as telas
frame_tela = Frame(janela,width= 235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

#Segundo frame "corpo"
frame_corpo = Frame(janela,width= 235, height=268)
frame_corpo.grid(row=1, column=0)



todos_valores = ''

def obter_valores(event):
    global todos_valores
    
    todos_valores = todos_valores + str(event) 
  
    valor_texto.set(todos_valores)

#Função de calculo

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


#Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2,padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 18',fg=cor2,bg=cor3)
app_label.place(x=0,y=0)

#Criando os botões
bt_1 = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_1.place(x=0,y=0)

bt_2 = Button(frame_corpo, command= lambda: obter_valores('%'),text="%", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_2.place(x=118, y=0)

bt_3 = Button(frame_corpo,command= lambda: obter_valores('/'),text="/", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_3.place(x=177,y=0)

bt_4 = Button(frame_corpo,command= lambda: obter_valores('7'),text="7", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_4.place(x=0, y=52)
bt_5 = Button(frame_corpo,command= lambda: obter_valores('8'),text="8", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_5.place(x=59, y=52)
bt_6 = Button(frame_corpo,command= lambda: obter_valores('9'),text="9", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_6.place(x=118, y=52)
bt_7 = Button(frame_corpo,command= lambda: obter_valores('*'),text="*", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_7.place(x=177,y=52)

bt_8 = Button(frame_corpo,command= lambda: obter_valores('4'),text="4", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_8.place(x=0, y=104)
bt_9 = Button(frame_corpo,command= lambda: obter_valores('5'),text="5", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_9.place(x=59, y=104)
bt_10 = Button(frame_corpo,command= lambda: obter_valores('6'),text="6", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_10.place(x=118, y=104)
bt_11= Button(frame_corpo,command= lambda: obter_valores('-'),text="-", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_11.place(x=177,y=104)

bt_12 = Button(frame_corpo,command= lambda: obter_valores('1'),text="1", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_12.place(x=0, y=156)
bt_13 = Button(frame_corpo,command= lambda: obter_valores('2'),text="2", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_13.place(x=59, y=156)
bt_14 = Button(frame_corpo,command= lambda: obter_valores('3'),text="3", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_14.place(x=118, y=156)
bt_15 = Button(frame_corpo,command= lambda: obter_valores('+'),text="+", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_15.place(x=177,y=156)

bt_16 = Button(frame_corpo,command= lambda: obter_valores('0'),text="0", width=11, height=2, bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_16.place(x=0,y=208)
bt_17 = Button(frame_corpo,command= lambda: obter_valores('.'),text=".", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_17.place(x=118, y=208)
bt_15 = Button(frame_corpo,command= calcular,text="=", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
bt_15.place(x=177,y=208)

#funções para as operações matematica


janela.mainloop()