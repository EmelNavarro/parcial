import sys
import re
from lineaDeComando import LineaDeComando
from ExpresionRegular import ExpresionRegular




def main(self):
	self=sys.argv
	if __name__ == '__main__': 
    		if len(sys.argv) >= 3: 
        		print ("La cantidad de argumentos ingresada no es correcta")

	palabra = sys.argv[1] 
	expresionRegular=ExpresionRegular(palabra)
	expresionRegular.ValidarExpresion()