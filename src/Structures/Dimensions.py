"""
Clase Dimensions que almacena la informacion de la dimension de una variable
Los atributos son lowerboud, upperbound y m. Todos de tipo int
"""
class Dimensions(object):

	"""
	Inicializa los atributos
	"""
	def __init__(self, lower=None, upper=None, m=None):
		self.lower = lower
		self.upper = upper
		self.m = m

	"""
	Regresa el limite inferior
	"""
	def getLowerBound(self):
		return self.lower

	"""
	Regresa el limite superior
	"""
	def getUpperBound(self):
		return self.upper

	"""
	Regresa la M
	"""
	def getM(self):
		return self.m

	"""
	Asigna el limite inferior
	"""
	def setLowerBound(self, lowerBound):
		self.lower = lowerBound

	"""
	Asigna el limite superior
	"""
	def setUpperBound(self, upperBound):
		self.upper = upperBound

	"""
	Asigna la M
	"""
	def setM(self, m):
		self.m = m

