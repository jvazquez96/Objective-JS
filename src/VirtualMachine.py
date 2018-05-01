import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Structures.Quadruple import Quadruple
from Structures.Stack import Stack

CONST_GLOBAL_BOTTOM_INT = 1000
CONST_GLOBAL_BOTTOM_FLOAT = 2000
CONST_GLOBAL_BOTTOM_CHAR = 3000
CONST_GLOBAL_BOTTOM_STRING = 4000
CONST_GLOBAL_BOTTOM_BOOLEAN = 5000
CONST_GLOBAL_BOTTOM_NULL = 6000

CONST_GLOBAL_TOP_INT = 1999
CONST_GLOBAL_TOP_FLOAT = 2999
CONST_GLOBAL_TOP_CHAR = 3999
CONST_GLOBAL_TOP_STRING = 4999
CONST_GLOBAL_TOP_BOOLEAN = 5999
CONST_GLOBAL_TOP_NULL = 6999

CONST_LOCAL_BOTTOM_INT = 7000
CONST_LOCAL_BOTTOM_FLOAT = 8000
CONST_LOCAL_BOTTOM_CHAR = 9000
CONST_LOCAL_BOTTOM_STRING = 10000
CONST_LOCAL_BOTTOM_BOOLEAN = 11000
CONST_LOCAL_BOTTOM_NULL = 12000

CONST_LOCAL_TOP_INT = 7999
CONST_LOCAL_TOP_FLOAT = 8999
CONST_LOCAL_TOP_CHAR = 9999
CONST_LOCAL_TOP_STRING = 10999
CONST_LOCAL_TOP_BOOLEAN = 11999
CONST_LOCAL_TOP_NULL = 12999

CONST_TEMPORAL_BOTTOM_INT = 13000
CONST_TEMPORAL_BOTTOM_FLOAT = 14000
CONST_TEMPORAL_BOTTOM_CHAR = 15000
CONST_TEMPORAL_BOTTOM_STRING = 16000
CONST_TEMPORAL_BOTTOM_BOOLEAN = 17000
CONST_TEMPORAL_BOTTOM_NULL = 18000

CONST_TEMPORAL_TOP_INT = 13999
CONST_TEMPORAL_TOP_FLOAT = 14999
CONST_TEMPORAL_TOP_CHAR = 15999
CONST_TEMPORAL_TOP_STRING = 16999
CONST_TEMPORAL_TOP_BOOLEAN = 17999
CONST_TEMPORAL_TOP_NULL = 17999

"""
Clase Memory que almacena los 3 diccionarios utilizados
para separar la memoria en constantes, locales y temporales
"""
class Memory():

	def __init__(self, locals, temps, constants):
		# int, float, char, string, boolean, null
		self.locals = locals
		self.temps = temps
		self.constants = constants

	def saveMemory(self, locals, temps, constants):
		self.locals = locals
		self.temps = temps
		self.constants = constants

	def getMemory(self):
		return self.locals, self.temps, self.constants

	"""
	Clase VirtualMachine, esta clase itera sobre todos los cuadruplos
	que lee desde un archivo.obj y realiza acciones dependiendo
	de la operacion.
	"""
class VirtualMachine(object):

	"""
	Función que almacena todos los cuadruplos en un arreglo
	e inicializa la memoria inicial.
	"""
	def __init__(self):
		self.quadruples = []
		with open ('archivo.obj', 'r') as file:
			for line in file:
				line = line[:-1]
				data = line.split(',')
				quadruple = Quadruple(data[0], data[1], data[2], data[3], data[4])
				self.quadruples.append(quadruple)
						# int, float, char, string, boolean, null
		self.constants = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.locals = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.temps = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.new_locals = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.new_temps = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.new_constants = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.object_contexts = dict()
		self.quadruple_pointer = 0
		self.pointer = Stack()
		self.context_stack = Stack()
		self.return_values = Stack()
		self.start()

	"""
	Función que itera sobre todos los cuadruplos y realiza una accion
	dependiendo del operador
	"""
	def start(self):
		while (self.quadruple_pointer < len(self.quadruples)):
			next_quadruple = self.quadruples[self.quadruple_pointer]
			address = next_quadruple.getResult()
			operator = int(next_quadruple.getOperator())
			operand1 = next_quadruple.getOperand1()
			operand2 = next_quadruple.getOperand2()

			# next_quadruple.print()
			if (address != "None" and address[0] != '(') and address[0] != '%':
				address = int(address)

			if operator == 1: # GOTO
				self.quadruple_pointer = int(address) - 2
			elif operator == 2: # GOTO False
				value = self.getValue(operand1)
				if not value:
					self.quadruple_pointer = int(address)-2
			elif operator == 3: # SUM
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 + val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 4: # Substraction
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 - val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 5: # igual
				if operand1[0] == '(':
					val = self.getValue(operand1)
					val = self.getValue(str(val))
				else:
					val = self.getValue(operand1)
				if not self.is_int(address):
					address = self.getValue(address)
				if self.is_constant(address):
					self.set_constant(address, val)
				elif self.is_local(address):
					self.set_local(self.locals, address, val)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, val)
			elif operator == 6: # read
				val = input("")
				val = self.get_actual_value(val)
					
				if operand1[0] == '(':
					address = self.getValue(operand1)
				else:
					address = operand1

				address = int(address)

				if self.is_constant(address):
					self.set_constant(address, val)
				elif self.is_local(address):
					self.set_local(self.locals, address, val)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, val)
			elif operator == 7: # division
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)

				if self.is_int_address(address):
					res = val1 // val2
				else:
					res = val1 / val2
					
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 8: # multiplicacion
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 * val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 9: # modulo
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)

				res = val1 % val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 10: # power ^
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = pow(val1,val2)
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 11: # not equal
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 != val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 12: # and
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 and val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 13: # or
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 or val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 14: # > (mayor que)
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)

				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
					
				res = val1 > val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 15: # < (menor que)
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 < val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 16: # >= mayor o igual
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 >= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 17: # menor o igual
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 <= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 18: # igual
				if operand1[0] == '(':
					val1 = self.getValue(operand1)
					val1 = self.getValue(str(val1))
				else:
					val1 = self.getValue(operand1)
				if operand2[0] == '(':
					val2 = self.getValue(operand2)
					val2 = self.getValue(str(val2))
				else:
					val2 = self.getValue(operand2)
				res = val1 == val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == 19: # isNull
				isNull = self.isNull(operand1)
				if self.is_constant(address):
					self.set_constant(address, isNull)
				elif self.is_local(address):
					self.set_local(self.locals, address, isNull)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, isNull)
			elif operator == 20: # isNotNull
				isNull = not self.isNull(operand1)
				if self.is_constant(address):
					self.set_constant(address, isNull)
				elif self.is_local(address):
					self.set_local(self.locals, address, isNull)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, isNull)
			elif operator == 21: # print
				if operand1[0] == '(':
					val = self.getValue(operand1)
					print(str(self.getValue(str(val))))
				else:
					val = self.getValue(operand1)
					print(str(val))
			elif operator == 22: # era
				if operand2 != "None": # We have an object context
					context = int(operand2)
					if context in self.object_contexts.keys():
						object_context = self.object_contexts[context]
						self.new_locals, self.new_temps, self.new_constants = object_context.getMemory()
					else:
						self.new_locals = [dict(), dict(), dict(), dict(), dict(), dict()]
						self.new_temps = [dict(), dict(), dict(), dict(), dict(), dict()]
						self.new_constants = [dict(), dict(), dict(), dict(), dict(), dict()]
						new_context = Memory(self.new_locals, self.new_temps, self.new_constants)
						self.object_contexts[context] = new_context
					current_context = Memory(self.locals, self.temps, self.constants)
					self.context_stack.push(current_context)
				else:
					current_context = Memory(self.locals, self.temps, self.constants)
					self.context_stack.push(current_context)
					self.new_locals = [dict(), dict(), dict(), dict(), dict(), dict()]
					self.new_temps = [dict(), dict(), dict(), dict(), dict(), dict()]
					self.new_constants = self.constants
			elif operator == 23: # param
				size = int(operand2)
				if self.is_local(address):
					start = 0;
					for i in range(size):
						address += start
						if operand1[0] != '%':
							new_operand = str(int(operand1) + i)
							val = self.getValue(new_operand)
						else:
							val = self.getValue(operand1)
						if self.is_local(address):
							self.set_local(self.new_locals, address, val)
						start = 1
				elif self.is_constant(address):
					start = 0;
					for i in range(size):
						address += start
						if operand1[0] != '%':
							new_operand = str(int(operand1) + i)
							val = self.getValue(new_operand)
						else:
							val = self.getValue(operand1)
						if self.is_constant(address):
							self.set_constant(self.new_constants, address, val)
						start = 1
				elif self.is_temporal(address):
					self.set_temporal(self.new_temps, address, val)
			elif operator == 24: # GO.SUB
				self.locals = self.new_locals
				self.temps = self.new_temps
				self.constants = self.new_constants
				self.pointer.push(self.quadruple_pointer + 1)
				self.quadruple_pointer = address - 2
			elif operator == 25: #endproc
				mem = self.context_stack.pop()
				self.locals, self.temps, self.constants = mem.getMemory()
				return_address = self.pointer.pop() - 1
				self.quadruple_pointer = return_address
			elif operator == 26: #return
				return_value = self.getValue(operand1)
				self.return_values.push(return_value)
			elif operator == 27: # save_return
				return_value = self.return_values.pop()
				if self.is_local(address):
					self.set_local(self.locals, address, return_value)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, return_value)
			elif operator == 28: # ver
				val = self.getValue(operand1)
				if not self.is_int(val):
					print("The indices of a list must be an integer")
					sys.exit(0)
				lowerBound = self.getValue(operand2)
				upperBound = self.getValue(address)
				if val < lowerBound or val >= upperBound:
					print("The indices must be between the boundaries")
					sys.exit(0)
			elif operator == 29: # attribute_access
				object_address = int(operand1)
				attribute_address = operand2
				dest_address = int(address)
				if object_address not in self.object_contexts.keys():
					print("Make sure to initalize the object before using it")
					sys.exit(0)
				object_context = self.object_contexts[object_address]
				current_context = Memory(self.locals, self.temps, self.constants)
				self.context_stack.push(current_context)
				self.locals, self.temps, self.constants = object_context.getMemory()
				value = self.getValue(attribute_address)
				self.return_values.push(value)
				mem = self.context_stack.pop()
				self.locals, self.temps, self.constatns = mem.getMemory()
			self.quadruple_pointer += 1


	"""
	Funcion que obteniene el valor literal de la variable
	"""
	def get_actual_value(self, value):
		if self.is_int(value):
			return int(value)
		elif self.is_float(value):
			return float(value)
		elif value == 'true':
			return True
		elif value == 'false':
			return False
		return value

	"""
	Funcion que intenta castear un parametro a int.
	El parametro es posiblemente int.
	Regresa un booleano
	"""
	def is_int(self, num):
		try:
			int(num)
			return True
		except ValueError:
			return False

	"""
	Funcion que intenta castear un parametro a float.
	El parametro es posiblemente float.
	Regresa un booleano
	"""
	def is_float(self, num):
		try:
			float(num)
			return True
		except ValueError:
			return False

	"""
	Funcion que obtiene el valor de una direccion. Dependiendo
	de la direccion y del formato va a ser el valor de retorno
	Regresa un el valor de la variable apuntado por la direccion
	"""
	def getValue(self, address):
		if self.is_actual_value(address):
			address = address[1:]
			return self.get_actual_value(address)
		elif self.is_address(address):
			return self.get_value_pointed_by_address(address)
		elif self.is_constant(int(address)):
			return self.get_constant(int(address))
		elif self.is_local(int(address)):
			return self.get_local(int(address))
		elif self.is_temporal(int(address)):
			return self.get_temporal(int(address))

	"""
	Función que verifica si la direccion inicia con un %.
	El parametro es de tipo String.
	Regresa un booleano
	"""
	def is_actual_value(self, address):
		return address.find("%") != -1

	"""
	Función que verifica si la direccion que se 
	recibe es un apuntador a otra direccion.
	El parametro es de tipo string.
	Regresa un booleano
	"""
	def is_address(self, address):
		return address[0] == '('

	"""
	Función que verifica si la direccion esta dentro
	del rango de constantes
	El parametro es de tipo int.
	Regresa un booleano
	"""
	def is_constant(self, address):
		return CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_NULL

	"""
	Función que verifica si la direccion esta dentro
	del rango de locales
	El parametro es de tipo int.
	Regresa un booleano
	"""
	def is_local(self, address):
		return CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_NULL

	"""
	Función que verifica si la direccion esta dentro
	del rango de temporales
	El parametro es de tipo int.
	Regresa un booleano
	"""
	def is_temporal(self, address):
		return CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_NULL


	"""
	Función que obtiene una direccion la cual
	es apuntada por el parametro
	El parametro es de tipo int.
	Regresa un int
	"""
	def get_value_pointed_by_address(self, address):
		new_address = address[1:-1]
		if self.is_constant(int(new_address)):
			new_address_2 = self.get_constant(int(new_address))
		elif self.is_local(int(new_address)):
			new_address_2 = self.get_local(int(new_address))
		elif self.is_temporal(int(new_address)):
			new_address_2 = self.get_temporal(int(new_address))

		return new_address_2

	"""
	Función que obtiene el valor apuntado por una direccion
	global. Si no existe la direccion regresa un mensaje de error
	El parametro es de tipo int.
	Regresa un int
	"""
	def get_constant(self, address):
		if CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_INT:
			if address not in self.constants[0]:
				print("A global int variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[0][address]
		elif CONST_GLOBAL_BOTTOM_FLOAT <= address <= CONST_GLOBAL_TOP_FLOAT:
			if address not in self.constants[1]:
				print("A global float variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[1][address]
		elif CONST_GLOBAL_BOTTOM_CHAR <= address <= CONST_GLOBAL_TOP_CHAR:
			if address not in self.constants[2]:
				print("A global char variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[2][address]
		elif CONST_GLOBAL_BOTTOM_STRING <= address <= CONST_GLOBAL_TOP_STRING:
			if address not in self.constants[3]:
				print("A global string variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[3][address]
		elif CONST_GLOBAL_BOTTOM_BOOLEAN <= address <= CONST_GLOBAL_TOP_BOOLEAN:
			if address not in self.constants[4]:
				print("A global boolean variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[4][address]
		elif CONST_GLOBAL_BOTTOM_NULL <= address <= CONST_GLOBAL_TOP_NULL:
			if address not in self.constants[5]:
				print("A global null variable is used but not intialized")
				sys.exit(0)
			else:
				return self.constants[5][address]

	"""
	Función que obtiene almacena un valor en una la direccion que se recibe
	como parametro
	El parametro address es de tipo int.
	El parametro value puede ser de cualquier tipo
	"""
	def set_constant(self, address, value):
		if CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_INT:
			self.constants[0][address] = value
		elif CONST_GLOBAL_BOTTOM_FLOAT <= address <= CONST_GLOBAL_TOP_FLOAT:
			self.constants[1][address] = value
		elif CONST_GLOBAL_BOTTOM_CHAR <= address <= CONST_GLOBAL_TOP_CHAR:
			self.constants[2][address] = value
		elif CONST_GLOBAL_BOTTOM_STRING <= address <= CONST_GLOBAL_TOP_STRING:
			self.constants[3][address] = value
		elif CONST_GLOBAL_BOTTOM_BOOLEAN <= address <= CONST_GLOBAL_TOP_BOOLEAN:
			self.constants[4][address] = value
		elif CONST_GLOBAL_BOTTOM_NULL <= address <= CONST_GLOBAL_TOP_NULL:
			self.constants[5][address] = value

	"""
	Función que obtiene el valor apuntado por una direccion
	local. Si no existe la direccion regresa un mensaje de error
	El parametro es de tipo int.
	Regresa un int
	"""
	def get_local(self, address):
		if CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_INT:
			if address not in self.locals[0]:
				print("A local int variable is used but not intialized")
			else:
				return self.locals[0][address]
		elif CONST_LOCAL_BOTTOM_FLOAT <= address <= CONST_LOCAL_TOP_FLOAT:
			if address not in self.locals[1]:
				print("A local float variable is used but not initialized")
			else:
				return self.locals[1][address]
		elif CONST_LOCAL_BOTTOM_CHAR <= address <= CONST_LOCAL_TOP_CHAR:
			if address not in self.locals[2]:
				print("A local char variable is used but not initialized")
			else:
				return self.locals[2][address]
		elif CONST_LOCAL_BOTTOM_STRING <= address <= CONST_LOCAL_TOP_STRING:
			if address not in self.locals[3]:
				print("A local string variable is used but not initialized")
			else:
				return self.locals[3][address]
		elif CONST_LOCAL_BOTTOM_BOOLEAN <= address <= CONST_LOCAL_TOP_BOOLEAN:
			if address not in self.locals[4]:
				print("A local boolean variable is used but not initialized")
			else:
				return self.locals[4][address]
		elif CONST_LOCAL_BOTTOM_NULL <= address <= CONST_LOCAL_TOP_NULL:
			if address not in self.locals[5]:
				print("A local null variable is used but not initialized")
			else:
				return self.locals[5][address]

	"""
	Función que obtiene almacena un valor en una la direccion que se recibe
	como parametro
	El parametro address es de tipo int.
	El parametro value puede ser de cualquier tipo
	"""
	def set_local(self, context, address, value):
		if CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_INT:
			context[0][address] = value
		elif CONST_LOCAL_BOTTOM_FLOAT <= address <= CONST_LOCAL_TOP_FLOAT:
			context[1][address] = value
		elif CONST_LOCAL_BOTTOM_CHAR <= address <= CONST_LOCAL_TOP_CHAR:
			context[2][address] = value
		elif CONST_LOCAL_BOTTOM_STRING <= address <= CONST_LOCAL_TOP_STRING:
			context[3][address] = value
		elif CONST_LOCAL_BOTTOM_BOOLEAN <= address <= CONST_LOCAL_TOP_BOOLEAN:
			context[4][address] = value
		elif CONST_LOCAL_BOTTOM_NULL <= address <= CONST_LOCAL_TOP_NULL:
			context[5][address] = value

	"""
	Función que obtiene almacena un valor en una la direccion que se recibe
	como parametro
	El parametro address es de tipo int.
	El parametro value puede ser de cualquier tipo
	"""
	def set_temporal(self, context, address, value):
		if CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_INT:
			context[0][address] = value
		elif CONST_TEMPORAL_BOTTOM_FLOAT <= address <= CONST_TEMPORAL_TOP_FLOAT:
			context[1][address] = value
		elif CONST_TEMPORAL_BOTTOM_CHAR <= address <= CONST_TEMPORAL_TOP_CHAR:
			context[2][address] = value
		elif CONST_TEMPORAL_BOTTOM_STRING <= address <= CONST_TEMPORAL_TOP_STRING:
			context[3][address] = value
		elif CONST_TEMPORAL_BOTTOM_BOOLEAN <= address <= CONST_TEMPORAL_TOP_BOOLEAN:
			context[4][address] = value
		elif CONST_TEMPORAL_BOTTOM_NULL <= address <= CONST_TEMPORAL_TOP_NULL:
			context[5][address] = value

	"""
	Función que obtiene el valor apuntado por una direccion
	local. Si no existe la direccion regresa un mensaje de error
	El parametro es de tipo int.
	Regresa un int
	"""
	def get_temporal(self, address):
		if CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_INT:
			return self.temps[0][address]
		elif CONST_TEMPORAL_BOTTOM_FLOAT <= address <= CONST_TEMPORAL_TOP_FLOAT:
			return self.temps[1][address]
		elif CONST_TEMPORAL_BOTTOM_CHAR <= address <= CONST_TEMPORAL_TOP_CHAR:
			return self.temps[2][address]
		elif CONST_TEMPORAL_BOTTOM_STRING <= address <= CONST_TEMPORAL_TOP_STRING:
			return self.temps[3][address]
		elif CONST_TEMPORAL_BOTTOM_BOOLEAN <= address <= CONST_TEMPORAL_TOP_BOOLEAN:
			return self.temps[4][address]
		elif CONST_TEMPORAL_BOTTOM_NULL <= address <= CONST_TEMPORAL_TOP_NULL:
			return self.temps[5][address]

	"""
	Funcion que verifica si la direccion que se recibe
	como parametro apunta a algun entero.
	El parametro es de tipo int.
	Regresa un booleano
	"""
	def is_int_address(self, address):
		if address >= CONST_GLOBAL_BOTTOM_INT or address <= CONST_GLOBAL_TOP_INT:
			return True
		elif address >= CONST_LOCAL_BOTTOM_INT or address <= CONST_LOCAL_TOP_INT:
			return True
		elif address >= CONST_TEMPORAL_BOTTOM_INT or address <= CONST_TEMPORAL_TOP_INT:
			return True
		else:
			return False

	"""
	Funcion que verifica si la direccion se encuentra en el rango de 
	nullos
	Regresa un booleano
	"""
	def isNull(self, address):
		address = int(address)
		if address in self.constants[5] or address in self.locals[5]:
			return False
		else:
			return True