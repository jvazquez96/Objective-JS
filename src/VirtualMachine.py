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

class Memory():

	def __init__(self, locals, temps):
					# int, float, char, string, boolean, null
		self.locals = locals
		self.temps = temps

	def saveMemory(self, locals, temps):
		self.locals = locals
		self.temps = temps

	def getMemory(self):
		return self.locals, self.temps


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
		self.new_locals = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.new_temps = [dict(), dict(), dict(), dict(), dict(), dict()]
		self.quadruple_pointer = 0
		self.pointer = Stack()
		self.context_stack = Stack()
		self.return_values = Stack()
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

			# next_quadruple.print()

			if address != "None":
				address = int(address)

			if operator == "GO.TO":
				self.quadruple_pointer = int(address) - 2
			elif operator == "GO.TOFALSE":
				value = self.getValue(operand1)
				if not value:
					self.quadruple_pointer = int(address)-2
			elif operator == "resetAddress":
				self.resetMemory()
			elif operator == "+":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 + val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "-":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 - val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "=":
				val = self.getValue(operand1)
				if self.is_constant(address):
					self.set_constant(address, val)
				elif self.is_local(address):
					self.set_local(self.locals, address, val)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, val)
			elif operator == "read":
				val = int(input(""))
				address = int(next_quadruple.getOperand1())
				if self.is_constant(address):
					self.set_constant(address, val)
				elif self.is_local(address):
					self.set_local(self.locals, address, val)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, val)
			elif operator == "/":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 / val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "*":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 * val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "^":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = pow(val1,val2)
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "!=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 != val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "&&":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 and val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "||":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 or val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == ">":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 > val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "<":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 < val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == ">=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 >= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "<=":
				val1 = self.getValue(operand1)
				val2 = self.getValue(operand2)
				res = val1 <= val2
				if self.is_constant(address):
					self.set_constant(address, res)
				elif self.is_local(address):
					self.set_local(self.locals, address, res)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, res)
			elif operator == "print":
				val = self.getValue(operand1)
				print(str(val))
			elif operator == "ERA":
				current_context = Memory(self.locals, self.temps)
				self.context_stack.push(current_context)
				self.new_locals = [dict(), dict(), dict(), dict(), dict(), dict()]
				self.new_temps = [dict(), dict(), dict(), dict(), dict(), dict()]
			elif operator == "param":
				val = self.getValue(operand1)
				if self.is_local(address):
					self.set_local(self.new_locals, address, val)
				elif self.is_temporal(address):
					self.set_temporal(self.new_temps, address, val)
			elif operator == "GO.SUB":
				self.locals = self.new_locals
				self.temps = self.new_temps
				self.pointer.push(self.quadruple_pointer + 1)
				self.quadruple_pointer = address - 2
			elif operator == "endproc":
				mem = self.context_stack.pop()
				self.locals, self.temps = mem.getMemory()
				return_address = self.pointer.pop() - 1
				self.quadruple_pointer = return_address
			elif operator == "return":
				return_value = self.getValue(operand1)
				self.return_values.push(return_value)
			elif operator == "save_return":
				return_value = self.return_values.pop()
				if self.is_local(address):
					self.set_local(self.locals, address, return_value)
				elif self.is_temporal(address):
					self.set_temporal(self.temps, address, return_value)
			elif operator == "VER":
				val = self.getValue(operand1)
				if not self.is_int(val):
					print("The indices of a list must be an integer")
					sys.exit(0)

				lowerBound = self.getValue(operand2)
				upperBound = address
				if val < lowerBound or val > upperBound:
					print("The indices must be between the boundaris")
					sys.exit(0)


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
		elif self.is_address(address):
			return self.get_value_pointed_by_address(address)
		elif self.is_constant(int(address)):
			return self.get_constant(int(address))
		elif self.is_local(int(address)):
			return self.get_local(int(address))
		elif self.is_temporal(int(address)):
			return self.get_temporal(int(address))

	def is_actual_value(self, address):
		return address.find("%") != -1

	def is_address(self, address):
		return address[0] == '('

	def is_constant(self, address):
		return CONST_GLOBAL_BOTTOM_INT <= address <= CONST_GLOBAL_TOP_NULL

	def is_local(self, address):
		return CONST_LOCAL_BOTTOM_INT <= address <= CONST_LOCAL_TOP_NULL

	def is_temporal(self, address):
		return CONST_TEMPORAL_BOTTOM_INT <= address <= CONST_TEMPORAL_TOP_NULL

	def get_value_pointed_by_addres(address):
		new_address = address[1:-1]
		new_address = int(new_address)
		if self.is_global(new_address):
			return self.get_constant(new_address)
		elif self.is_local(new_address):
			return self.get_local(new_address)
		elif self.is_temporal(new_address):
			return self.get_temporal(new_address)

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