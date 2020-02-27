import re
"""cadena=("(AAA80)*856-(987899)"),^([(])([A-Z]{3})(([0-9]){2})([)])([*])([0-9]{3})([-])([(])([0-9]{6})([)])$"""
class ExpresionRegular:
	def __init__(self,Expresion):
		self.Expresion=Expresion
	def ValidarExpresion(self):
		ExpresionRegular=re.compile(r"([a-z]{20}?)")
		if ExpresionRegular.match(self.Expresion)is not None:
			print (self.Expresion,", es una palabra correcta")
		else: 
			print(self.Expresion,", no es una palabra correcta")
