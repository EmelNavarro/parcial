import sys 


def LineaDeComando():
	for  elements in sys.argv:
		print (elements)
	return sys.argv	
print("la cantidad de argumentos es :",len(sys.argv))
		
		


