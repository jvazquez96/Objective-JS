import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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

class_stack = list()


class Class(object):

	def __init__(self):
		# int, float, char, string, boolean, null
		self.memory = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.method_stack = list()
		self.name = ""

class Method(object):

	def __init__(self):
							# int, float, char, string, boolean, null
		self.temp_memory = [dict(), dict(), dict(), dict(), dict(), dict()]
								# int, float, char, string, boolean, null
		self.local_memory = [dict(), dict(), dict(), dict(), dict(), dict()]

class VirtualMachine(object):

	def __init__(self):
		with open ('archivo.obj', 'r') as file:
			self.quadruples = file.readlines()
		list_splitted = self.quadruples[0].split( )
		for i in list_splitted:
			print(i)
		self.operation(list_splitted[0], list_splitted[1], list_splitted[2], list_splitted[3])
						# int, float, char, string, boolean, null
		self.constants = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.locals = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.temps = [dict(), dict(), dict(), dict(), dict(), dict()]

	def is_actual_value(self, address):
		return address.find("%") != -1

	def is_constant(self, address):
		return CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_NULL

	def is_local(self, address):
		return CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_NULL

	def is_temporal(self, address):
		return CONST_TEMPORAL_TOP_INT <= address <= CONST_TEMPORAL_TOP_NULL

	def get_constant(self, address):
		if CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_INT:
			return self.constants[0][address]
		elif CONST_GLOBAL_BOTTOM_FLOAT <= address <= CONST_GLOBAL_TOP_FLOAT:
			return self.constants[1][address]
		elif CONST_GLOBAL_BOTTOM_CHAR <= address <= CONST_GLOBAL_TOP_CHAR:
			return self.constants[2][address]
		elif CONST_GLOBAL_BOTTOM_STRING <= address <= CONST_GLOBAL_TOP_STRING:
			return self.constants[3][address]
		elif CONST_GLOBAL_BOTTOM_BOOLEAN <= address <= CONST_GLOBAL_TOP_BOOLEAN:
			return self.constants[4][address]
		elif CONST_GLOBAL_BOTTOM_NULL <= address <= CONST_GLOBAL_TOP_NULL:
			return self.constants[5][address]

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

	def get_local(self, address):
		if CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_INT:
			return self.locals[0][address]
		elif CONST_LOCAL_BOTTOM_FLOAT <= address <= CONST_LOCAL_TOP_FLOAT:
			return self.locals[1][address]
		elif CONST_LOCAL_BOTTOM_CHAR <= address <= CONST_LOCAL_TOP_CHAR:
			return self.locals[2][address]
		elif CONST_LOCAL_BOTTOM_STRING <= address <= CONST_LOCAL_TOP_STRING:
			return self.locals[3][address]
		elif CONST_LOCAL_BOTTOM_BOOLEAN <= address <= CONST_LOCAL_TOP_BOOLEAN:
			return self.locals[4][address]
		elif CONST_LOCAL_BOTTOM_NULL <= address <= CONST_LOCAL_TOP_NULL:
			return self.locals[5][address]

	def set_local(self, address, value):
		if CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_INT:
			self.locals[0][address] = value
		elif CONST_LOCAL_BOTTOM_FLOAT <= address <= CONST_LOCAL_TOP_FLOAT:
			self.locals[1][address] = value
		elif CONST_LOCAL_BOTTOM_CHAR <= address <= CONST_LOCAL_TOP_CHAR:
			self.locals[2][address] = value
		elif CONST_LOCAL_BOTTOM_STRING <= address <= CONST_LOCAL_TOP_STRING:
			self.locals[3][address] = value
		elif CONST_LOCAL_BOTTOM_BOOLEAN <= address <= CONST_LOCAL_TOP_BOOLEAN:
			self.locals[4][address] = value
		elif CONST_LOCAL_BOTTOM_NULL <= address <= CONST_LOCAL_TOP_NULL:
			self.locals[5][address] = value


	def get_value_from_memory(self, address):
		if self.is_constant(address):
			value = self.get_constant(address)

		return value

	def operation(self, op, left, right, dest):
		pass
		# if op == ""
