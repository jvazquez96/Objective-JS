from Structures.Info import Info
from Structures.FunctionsDirectory import FunctionsDirectory
from Structures.ParamTable import ParamTable
from Structures.Atts import Atts

class Classes(object):

	def __init__(self):
		self.name = None
		self.inherits = None
		self.constructors = []
		self.numberOfCons = 0
		self.attributes = None
		self.methods = None

	def setName(self, name):
		self.name = name

	def setInherits(self, inherits):
		self.inherits = inherits

	def setAttributes(self, attributes):
		self.attributes = attributes

	def getName(self):
		return self.name

	def getInherits(self):
		return self.inherits

	def addConstructorParams(self, ParamTable):
		self.constructors.append(ParamTable)
		self.numberOfCons += 1

	def addMethodsTable(self, FunctionsDirectory):
		self.methods = FunctionsDirectory

	def printConstuctorTable(self):
		for key, value in self.constructors[self.numberOfCons-1].getParameters().items():
			print("ID: " + key)
			print("Type: " + str(value.getType()))
			print("Size: " + str(value.getListSize()))
			print("Address: " + str(value.getAddress()))

	def printAtts(self):
		for key, value in self.attributes.items():
			print("ID: " + str(key))
			print("Type: " + str(value.getType()))
			print("Accesible: " + str(value.isAccessible()))

	def printMethods(self):
		for key, value in self.methods.getDirectory().items():
			print("Function: " + key)
			print("Accessibility: " + str(value.getAccessibility()))
			for key2, value2 in value.getParamTable().getParameters().items():
				print("Var name: " + key2)

