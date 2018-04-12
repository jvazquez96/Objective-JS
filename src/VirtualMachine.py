import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Structures.Quadruple import Quadruple

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

class VirtualMachine(object):

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
		self.quadruple_pointer = 0
		self.start()

	def resetMemory(self):
		for localMemory, tempMemory in zip(self.locals, self.temps):
			localMemory.clear()
			tempMemory.clear()

	def start(self):
		while (self.quadruple_pointer < len(self.quadruples)):
			next_quadruple = self.quadruples[self.quadruple_pointer]
			address = next_quadruple.getResult()
			operator = next_quadruple.getOperator()
			operand1 = next_quadruple.getOperand1()
			operand2 = next_quadruple.getOperand2()
			if address != "None" and operator != "param":
				address = int(address)
		# if op == "GO.TO":
		# 	self.quadruple_pointer = int(address) - 1
			if operator == "resetAddress":
				self.resetMemory()
			elif operator == "+":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 + val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "-":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 - val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "=":
				val = self.getValue(operand1)
				if self.is_constant(address):
					self.set_constant(address, val)
				elif self.is_local(address):
					self.set_local(address, val)
				elif self.is_temporal(address):
					self.set_temporal(address, val)
			elif operator == "/":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 / val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "*":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 * val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "!=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 != val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "&&":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 and val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "||":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 or val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == ">":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 > val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "<":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 < val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == ">=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 >= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "<=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 <= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(address, res)
				elif self.is_temporal(address):
					self.set_temporal(address, res)
			elif operator == "print":
				val = self.getValue(operand1)
				print(str(val))

			self.quadruple_pointer += 1

	def get_actual_value(self, value):
		value = value[1:]
		if self.is_int(value):
			return int(value)
		elif self.is_float(value):
			return float(value)
		elif value == 'true':
			return True
		elif value == 'false':
			return False
		return value

	def is_int(self, num):
		try:
			int(num)
			return True
		except ValueError:
			return False

	def is_float(self, num):
		try:
			float(num)
			return True
		except ValueError:
			return False

	def getValue(self, address):
		if self.is_actual_value(address):
			return self.get_actual_value(address)
		elif self.is_constant(int(address)):
			return self.get_constant(int(address))
		elif self.is_local(int(address)):
			return self.get_local(int(address))
		elif self.is_temporal(int(address)):
			return self.get_temporal(int(address))

	def is_actual_value(self, address):
		return address.find("%") != -1

	def is_constant(self, address):
		return CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_NULL

	def is_local(self, address):
		return CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_NULL

	def is_temporal(self, address):
		return CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_NULL

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

	def set_temporal(self, address, value):
		if CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_INT:
			self.temps[0][address] = value
		elif CONST_TEMPORAL_BOTTOM_FLOAT <= address <= CONST_TEMPORAL_TOP_FLOAT:
			self.temps[1][address] = value
		elif CONST_TEMPORAL_BOTTOM_CHAR <= address <= CONST_TEMPORAL_TOP_CHAR:
			self.temps[2][address] = value
		elif CONST_TEMPORAL_BOTTOM_STRING <= address <= CONST_TEMPORAL_TOP_STRING:
			self.temps[3][address] = value
		elif CONST_TEMPORAL_BOTTOM_BOOLEAN <= address <= CONST_TEMPORAL_TOP_BOOLEAN:
			self.temps[4][address] = value
		elif CONST_TEMPORAL_BOTTOM_NULL <= address <= CONST_TEMPORAL_TOP_NULL:
			self.temps[5][address] = value

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



	def get_value_from_memory(self, address):
		if self.is_constant(address):
			value = self.get_constant(address)

		return value