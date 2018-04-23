from Structures.Info import Info
from Structures.FunctionsDirectory import FunctionsDirectory
from Structures.ParamTable import ParamTable
from Structures.Atts import Atts
import sys

class Classes(object):

	def __init__(self):
		self.name = None
		self.inherits = None
		self.constructors = []
		self.numberOfCons = 0
		self.constructorsVerified = 0
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

	def getMethods(self):
		return self.methods

	def addConstructorParams(self, ParamTable):
		self.constructors.append(ParamTable)
		self.numberOfCons += 1

	def addMethodsTable(self, FunctionsDirectory):
		self.methods = FunctionsDirectory

	def copyInfo(self, inherits):
		self.copyAtts(inherits)
		self.copyMethods(inherits)

	def verifyConstructorParams(self, params):
		if self.constructorsVerified == self.numberOfCons:
			print("Constructor implemented but not defined")
			sys.exit(0)
			
		params_declared = self.constructors[self.constructorsVerified].getParameters().items()
		real_params = params.getParameters().items()
		my_params = [] 
		iterator = 0

		if len(params_declared) != len(real_params):
			print("Wrong number of params in constructor")
			sys.exit()

		for key, value in params_declared:
			my_params.append(value)

		for key, value in real_params:
			if my_params[iterator].getId() != key or my_params[iterator].getType() != value.getType():
				print("Wrong param in constructor")
				sys.exit(0)
			iterator += 1

		self.constructorsVerified += 1

	def verifyMethod(self, function_name, argumentos, return_type):
		if function_name in self.methods.getDirectory().keys():
			declared = self.methods.getDirectory()[function_name].getParamTable().getParameters().items()
			used = argumentos.getParameters().items()
			aux = []
			iterator = 0

			if len(declared) != len(used):
				print("Wrong number of params in function")
				sys.exit(0)


			for key, value in declared:
				aux.append(value)

			for key, value in used:
				if aux[iterator].getId() != key or aux[iterator].getType() != value.getType():
					print("Wrong param in function")
					sys.exit(0)
				iterator += 1

			if return_type != self.methods.getDirectory()[function_name].getReturnType():
				print("Wrong returning type")
				sys.exit(0)
		else:
			print("Function " + function_name + " was not declared")
			sys.exit(0)

	def copyAtts(self, inherits):
		for key, value in inherits.attributes.items():
			if key in self.attributes.keys():
				print(key + " from " + inherits.getName() + " already defined in " + self.name)
				sys.exit(0)
			else:
				self.attributes[key] = value

	def copyMethods(self, inherits):
		for key, value in inherits.methods.getDirectory().items():
			if key in self.methods.getDirectory().keys():
				print(key + " from " + inherits.getName() + " already defined in " + self.name)
				sys.exit(0)
			else:
				self.methods.getDirectory()[key] = value

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
			print("Type: " + str(value.getReturnType()))
			for key2, value2 in value.getParamTable().getParameters().items():
				print("Var name: " + key2)

	def printInfo(self):
		print("Class name: " + self.name)
		print("Inherits: " + str(self.inherits))
		self.printAtts()
		self.printMethods()
