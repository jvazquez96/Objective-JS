"""
Clase Quadruple que representa a una estructura con 4 campos.
id = int
operator = string
operand1 = string
operand2 = string
result = string
"""
class Quadruple(object):

	"""
	Inicializa los atributos de la clase el id es un entero, el resto son strings
	"""
	def __init__(self, id, operator=None, operand1=None, operand2=None, result=None):
		self.id = id
		self.operator = operator
		self.operand1 = operand1
		self.operand2 = operand2
		self.result = result

	"""
	Regresa el ID del cuadruplo
	"""
	def getId(self):
		return self.id
	"""
	Regresa el operador del cuadruplo
	"""
	def getOperator(self):
		return self.operator

	"""
	Regresa el primer operando del quadruplo
	"""
	def getOperand1(self):
		return self.operand1

	"""
	Regresa el segundo operando del quadruplo
	"""
	def getOperand2(self):
		return self.operand2

	"""
	Regresa el resultado del quadruplo
	"""
	def getResult(self):
		return self.result

	"""
	Asigna el resutaldo en la posicion de resultado
	"""
	def setResult(self, result):
		self.result = result

	"""
	Imprime el cuadruplo con un buen formato
	"""
	def print(self):
		print(str(self.id) + " " + str(self.operator) + " " + str(self.operand1) + " " + str(self.operand2) + " " + str(self.result))

	"""
	Asigna el operador a un cuadruplo
	"""
	def setOperator(self, operator):
		self.operator = operator