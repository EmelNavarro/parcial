from tkinter import*
from Main import main

self=sys.argv
raiz= Tk()

raiz.title("ventanita")
raiz.resizable(False,False)

myFrame=Frame(raiz,width="350",height="350")
myFrame.pack()


milabel=Label(myFrame,text= "ingrese linea de comandos: ",font=("Comic Sans MS",12))
milabel.grid(row=0,column=0,sticky="e",padx=15,pady=15)

cuadrotextolineadecomando=Entry(myFrame)
cuadrotextolineadecomando.grid(row=0,column=1,sticky="e",padx=15,pady=15)
cuadrotextolineadecomando.config(justify="center")

milabel2=Label(myFrame,text= "la palabra ingresada es: ",font=("Comic Sans MS",12))
milabel2.grid(row=1,column=0,sticky="e",padx=15,pady=15)

cuadrotextovalidacion=Entry(myFrame)
cuadrotextovalidacion.grid(row=1,column=1,sticky="e",padx=15,pady=15)
cuadrotextovalidacion.config(justify="center")

botonvalidar=Button(raiz, text="validar", COMMAND=main(self))
botonvalidar.pack()



raiz.mainloop()
