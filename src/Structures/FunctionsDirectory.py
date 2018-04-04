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
			print("Error")
			sys.exit(0)
		else:
			self.directory[id].deleteTable()

	def getSymbolTable(self, id):
		return self.directory[id].getSymbolTable()

	def getDirectory(self):
		return self.directory

	def addInt(self, id, isParameter):
		self.directory[id].addInteger(isParameter)

	def addFloat(self, id, isParameter):
		self.directory[id].addFloat(isParameter)

	def addChar(self, id, isParameter):
		self.directory[id].addChar(isParameter)

	def addString(self, id, isParameter):
		self.directory[id].addString(isParameter)

	def addBool(self, id, isParameter):
		self.directory[id].addBool(isParameter)