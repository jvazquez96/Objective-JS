from Structures.Dimensions import Dimensions

"""
Clase Info que almacena la información de una variable.
La información que se guarda es:
tipo : int
isList: bool
listSize : int
dim : int
dimensions : Dimensions
"""
class Info(object):
	"""
	Inicializa la informacion de una variable
	"""
	def __init__(self, type=None, isList=None, listSize=0, dim = 0, dimensions = None, address = 0):
		if type is None:
			self._info = []
		else:
			self._info = [type, isList, listSize, dim, dimensions, address]
	"""
	Regresa la lista con la informacion de la variable
	"""
	def getInfo(self):
		return self._info
	"""
	Regresa el tipo de una variable, si no tiene informacion regresa una lista vacia
	"""
	def getType(self):
		if not self._info:
			return []
		else:
			return self._info[0]
	"""
	Asigna el tipo a de una variable
	"""
	def setType(self, type):
		self._info[0] = type
	"""
	Regresa un booleano indicando si es una lista o no.
	"""
	def isList(self):
		return self._info[1]
	"""
	Regresa el tamano de la lista
	"""
	def getListSize(self):
		return self._info[2]
	"""
	Regresa la cantidad de dimensiones de una lista
	"""
	def getDim(self):
		return self._info[3]
	"""
	Regresa la lista de dimensiones
	"""
	def getDimensions(self):
		return self._info[4]
	"""
	Regresa el limite inferior de una dimension que se recibe como parametro
	"""
	def getLowerBound(self, dim):
		return self._info[4][dim].getLowerBound()
	"""
	Regresa el limite superior de una dimension que se recibe como parametro
	"""
	def getUpperBound(self, dim):
		return self._info[4][dim].getUpperBound()
	"""
	Regresa la M de una dimension
	"""
	def getM(self, dim):
		return self._info[4][dim].getM()
	"""
	Regresa la direccion de la variable
	"""
	def getAddress(self):
		return self._info[5]