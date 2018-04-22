from Structures.SymbolTable import SymbolTable
from Structures.Stack import Stack
from Structures.ParamTable import ParamTable

class InfoDirectory(object):
	def __init__ (self, symbol_table=SymbolTable(), return_type=None):
		self.symbol_table = symbol_table
		self.return_type = None
		# Types of parameters [int, float, char, string, bool]
		self.parameters = [0, 0, 0, 0, 0]
		# Types of local variables [int, float, char, string, bool]
		self.local_variables = [0, 0, 0, 0, 0]
		# Types of tempral variables [int, float, char, string, bool]
		self.temporal_variables = [0, 0, 0, 0, 0]
		#
		self.parameters2 = []
		# Param table
		self.param_table = ParamTable()
		# Address where the function starts
		self.start_address = 0
		self.accessible = None

	def createInfo(self, symbol_table, return_type):
		self.symbol_table = symbol_table
		self.return_type = return_type

	def setReturnType(self, type):
		self.return_type = type

	def getParamTable(self):
		return self.param_table

	def getSymbolTable(self):
		return self.symbol_table

	def getReturnType(self):
		return self.return_type

	def getParams(self):
		return self.parameters2

	def getStartAddress(self):
		return self.start_address

	def getText(self):
		return self.text

	def setParamTable(self, paramTable):
		self.param_table = paramTable

	def setStartAddress(self, address):
		self.start_address = address
		self.text = "I'm being set"

	def deleteTable(self):
		self.symbol_table = SymbolTable()

	def addParameter(self, id, type, size):
		parameter = [id, type, size]
		self.parameters2.append(parameter)

	def addInteger(self, isParameter, n):
		if isParameter:
			self.parameters[0] += n
		else:
			self.local_variables[0] += n

	def addFloat(self, isParameter, n):
		if isParameter:
			self.parameters[1] += n
		else:
			self.local_variables[1] += n

	def addChar(self, isParameter, n):
		if isParameter:
			self.parameters[2] += n
		else:
			self.local_variables[2] += n

	def addString(self, isParameter, n):
		if isParameter:
			self.parameters[2] += n
		else:
			self.local_variables[2] += n

	def addBool(self, isParameter, n):
		if isParameter:
			self.parameters[3] += n
		else:
			self.local_variables[3] += n

	def addTemporaryInt(self, n):
		self.temporal_variables[0] += n

	def addTemporaryFloat(self, n):
		self.temporal_variables[1] += n

	def addTemporaryChar(self, n):
		self.temporal_variables[2] += n

	def addTemporaryString(self, n):
		self.temporal_variables[3] += n

	def addTemporaryBool(self, n):
		self.temporal_variables[4] += n


	def numberOfParameters(self):
		return sum(self.parameters)

	def numberOfLocalVariables(self):
		return sum(self.local_variables)

	def numberofTemporaryVariables(self):
		return sum(self.temporal_variables)

	def numberOfVariablesInt(self):
		return self.local_variables[0]
	def numberOfVariablesFloat(self):
		return self.local_variables[1]
	def numberOfVariablesChar(self):
		return self.local_variables[2]
	def numberOfVariablesString(self):
		return self.local_variables[3]
	def numberOfVariablesBool(self):
		return self.local_variables[4]


	def numberOfParametersInt(self):
		return self.parameters[0]
	def numberOfParametersFloat(self):
		return self.parameters[1]
	def numberOfParametersChar(self):
		return self.parameters[2]
	def numberOfParametersString(self):
		return self.parameters[3]
	def numberOfParametersBool(self):
		return self.parameters[4]

	def numberOfTemporaryInt(self):
		return self.temporal_variables[0]
	def numberOfTemporaryFloat(self):
		return self.temporal_variables[1]
	def numberOfTemporaryChar(self):
		return self.temporal_variables[2]
	def numberOfTemporaryString(self):
		return self.temporal_variables[3]
	def numberOfTemporaryBool(self):
		return self.temporal_variables[4]


	def getParameters(self):
		return self.parameters

	def getVariables(self):
		return self.local_variables

	def setAccessibility(self, accessibility):
		self.accessible = accessibility

	def getAccessibility(self):
		return self.accessible