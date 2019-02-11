from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

operacion=""
resultado=0
memoria=StringVar()
#------------------Pantalla------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="green",justify="right")

#------------------Pulsaciones Teclado------------------
def numeroPulsado(num):
    global operacion
    global resultado
            
    if operacion != "":
        numeroPantalla.set(num)
        operacion=""
    else:
        if (num=="."):
            if ("." in numeroPantalla.get()):
                pass
            else:
                numeroPantalla.set(numeroPantalla.get() + num)
        if (num=="CE"):
            numeroPantalla.set()
            resultado=0
            operacion=""
        else:
            numeroPantalla.set(numeroPantalla.get() + num)
        
                
#------------------Funcion suma---------------------
def suma(num):
    global operacion
    global resultado
    resultado+=float(num)
    operacion ="suma"
    numeroPantalla.set(resultado)
#---------------------Funcion Igual---------------------
def igual():
    global resultado
    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado=0

#------------------Fila1------------------
botonCE=Button(miFrame,text="CE",width=3,command=lambda:numeroPulsado("CE"))
botonCE.grid(row=2,column=1)
botonC=Button(miFrame,text="C",width=3,command=lambda:numeroPulsado("C"))
botonC.grid(row=2,column=2)
botonBack=Button(miFrame,text="<-",width=3,command=lambda:numeroPulsado("Back"))
botonBack.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)

#------------------Fila2------------------
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3)
botonMult=Button(miFrame,text="x",width=3)
botonMult.grid(row=3,column=4)

#------------------Fila3------------------
boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=4,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
botonRest=Button(miFrame,text="-",width=3)
botonRest.grid(row=4,column=4)

#------------------Fila4------------------
boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
botonSum=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)

#------------------Fila5------------------
botonNegar=Button(miFrame,text="+-",width=3,command=lambda:numeroPulsado("negar"))
botonNegar.grid(row=6,column=1)
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=2)
botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado("."))
botonComa.grid(row=6,column=3)
botonIgual=Button(miFrame,text="=",width=3,command=lambda:igual())
botonIgual.grid(row=6,column=4)


raiz.mainloop()