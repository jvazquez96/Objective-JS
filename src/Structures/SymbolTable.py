from Structures.Info import Info
from Structures.Dimensions import Dimensions

"""
Clase SymbolTable que almacena en un diccionario la informacion 
de variables. El formato es diccionario donde la llave es el nombre de la variable y el valor es un objeto de tipo Info
"""
class SymbolTable(object):
	"""
	Inicia el diccionario vacio
	"""
	def __init__(self):
		self._symbols = dict()
	"""
	Ingresa un objeto de tipo Info en la llave de tipo string
	"""
	def push_frame(self, address, id, type=None, isList = None, listSize = 0, dim = 0, dimensions = None):
		self._symbols[id] = Info(type, isList, listSize, dim, dimensions, address);
	"""
	Regresa la cantidad de variables
	"""
	def size(self):
		return len(self._symbols)
	"""
	Regresa un objeto de tipo Info dada una llave. Si la llave no esta
	regresa una lista vacia
	"""
	def getContent(self, id):
		if id in self._symbols:
			return self._symbols[id]
		else:
			return []
	"""
	Regresa el diccionario de symbolos
	"""
	def getSymbols(self):
		return self._symbols
	"""
	Regresa la cantidad de dimensions de una variable
	"""
	def getDimensions(self, id):
		return self._symbols[id].getDim()