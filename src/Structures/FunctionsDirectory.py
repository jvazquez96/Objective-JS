import sys

class FunctionsDirectory(object):

	def __init__(self):
		self.directory = dict()

	def create_table(self, id, info):
		if id in self.directory:
			print("Syntax error!! Function already defined")
			sys.exit(0)
		else:
			self.directory[id] = info

	def remove_info(self, id):
		if id not in self.directory:
			sys.exit(0)
		else:
			self.directory[id].deleteTable()

	def addParam(self, id, name, value, size):
		self.directory[id].addParameter(name, value, size)

	def getInfoDirectory(self, id):
		return self.directory[id].getSymbolTable()

	def getTable(self, id):
		return self.directory[id]

	def getDirectory(self):
		return self.directory

	def addInt(self, id, isParameter, n):
		self.directory[id].addInteger(isParameter, n)

	def addFloat(self, id, isParameter, n):
		self.directory[id].addFloat(isParameter, n)

	def addChar(self, id, isParameter, n):
		self.directory[id].addChar(isParameter, n)

	def addString(self, id, isParameter, n):
		self.directory[id].addString(isParameter, n)

	def addBool(self, id, isParameter, n):
		self.directory[id].addBool(isParameter, n)

	def addNull(self, id, isParameter, n):
		self.directory[id].addNull(isParameter, n)

	def addTempInt(self, id, n):
		self.directory[id].addTemporaryInt(n)

	def addTempFloat(self, id, n):
		self.directory[id].addTemporaryFloat(n)

	def addTempChar(self, id, n):
		self.directory[id].addTemporaryChar(n)

	def addTempString(self, id, n):
		self.directory[id].addTemporaryString(n)

	def addTempBool(self, id, n):
		self.directory[id].addTemporaryBool(n)