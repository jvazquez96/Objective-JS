from Structures.SymbolTable import SymbolTable
class InfoDirectory(object):
	def __init__ (self, symbol_table=None, return_type=None):
		if symbol_table is None and return_type is None:
			self._info = [SymbolTable(), None]
		else:
			self._info = [symbol_table, return_type]
		# Types of parameters [int, float, char, string, bool]
		self.parameters = [0, 0, 0, 0, 0]
		# Types of local variables [int, float, char, string, bool]
		self.local_variables = [0, 0, 0, 0, 0]
		# Types of tempral variables [int, float, char, string, bool]
		self.temporal_variables = [0, 0, 0, 0, 0]

	def getInfo(self):
		return self._info

	def createInfo(self, symbol_table, return_type):
		self._info = InfoDirectory(symbol_table, return_type)

	def getSymbolTable(self):
		return self._info[0]

	def getReturnType(self):
		return self._info[1]

	def deleteTable(self):
		self._info[0] = SymbolTable()

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