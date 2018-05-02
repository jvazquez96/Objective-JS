from Structures.Info import Info
from Structures.FunctionsDirectory import FunctionsDirectory
from Structures.ParamTable import ParamTable
from Structures.Atts import Atts
import sys
"""
Clase Classess que almacena la informacion de una clase (Orientado a Objetos)
la informacion que almacena es su nombre, el nombre de la clase que hereda, la lista de constructores, el numero de constructores, el numero de constructores verificados, un objeto Atts que contiene a los atributos, un objeto methods que tiene el directorio de funciones (FunctionDirectory) de la clase y la direccion de inicio de todos los constructores
"""

class Classes(object):

	"""
	Inicializa los atributos de la clase en None o en []
	"""
	def __init__(self):
		self.name = None
		self.inherits = None
		self.constructors = []
		self.numberOfCons = 0
		self.constructorsVerified = 0
		self.attributes = None
		self.methods = None
		self.constructors_start_address = []
	"""
	Asigna el nombre de la clase
	"""
	def setName(self, name):
		self.name = name
	"""
	Asigna el nombre de la clase de la que hereda
	"""
	def setInherits(self, inherits):
		self.inherits = inherits

	"""
	Asigna los atributos de la clase
	"""
	def setAttributes(self, attributes):
		self.attributes = attributes
	"""
	Regresa los atributos de la clase
	"""
	def getAttributes(self):
		return self.attributes
	"""
	Regresa el nombre de la clase
	"""
	def getName(self):
		return self.name

	"""
	Regresa el nombre de la clase que hereda
	"""
	def getInherits(self):
		return self.inherits

	"""
	Regresa los metodos
	"""
	def getMethods(self):
		return self.methods

	"""
	Regresa la cantidad de constructores
	"""
	def getNumberOfConstructors(self):
		return self.numberOfCons

	"""
	Agrega la direcccion de inicio de un constructor
	"""
	def addConstructorStartAddress(self, address):
		self.constructors_start_address.append(address)

	"""
	Regresa la direccion de inicio de un constructor
	"""
	def getStartAddress(self, pos):
		return self.constructors_start_address[pos]

	"""
	Agrega la tabla de parametros a un constructor
	"""
	def addConstructorParams(self, ParamTable):
		self.constructors.append(ParamTable)
		self.numberOfCons += 1

	"""
	Agrega la tabla de metodos
	"""
	def addMethodsTable(self, FunctionsDirectory):
		self.methods = FunctionsDirectory

	"""
	Copia la informacion de una clase
	"""
	def copyInfo(self, inherits):
		self.copyAtts(inherits)
		self.copyMethods(inherits)

	"""
	Verifica que el constructor este correctamente implementado
	"""
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

	"""
	Verifica si un constructor esta implementado de manera correcta
	"""
	def isConstructorCorrectlyImplemented(self, params, constructor_count):
		constructor_params = self.constructors[constructor_count].getParameters().items()
		if len(constructor_params) != len(params.getParameters()):
			return False

		for (key, paramInfo), (key2, constructorInfo) in zip(params.getParameters().items(), constructor_params):
			if len(paramInfo.getDimensions()) != len(constructorInfo.getDimensions()):
				return False
			if paramInfo.getListSize() != constructorInfo.getListSize():
				return False
			if paramInfo.getType() != constructorInfo.getType():
				return False
			for dimP, dimC in zip(paramInfo.getDimensions(), constructorInfo.getDimensions()):
				if dimP.getUpperBound() != dimC.getUpperBound():
					return False
		return True


	"""
	Verifica si un metodo esta implementado de manera correcta
	"""
	def verifyMethod(self, function_name, argumentos, return_type):
		if function_name in self.methods.getDirectory().keys():
			declared = self.methods.getDirectory()[function_name].getParamTable().getParameters().items()
			used = argumentos.getParameters().items()
			aux = []
			iterator = 0

			if len(declared) != len(used):
				print("Wrong number of params in function " + function_name)
				sys.exit(0)


			for key, value in declared:
				aux.append(value)

			for key, value in used:
				if aux[iterator].getId() != key or aux[iterator].getType() != value.getType():
					print("Wrong param in function " + function_name)
					sys.exit(0)
				iterator += 1

			if return_type != self.methods.getDirectory()[function_name].getReturnType():
				print("Wrong returning type in function " + function_name)
				sys.exit(0)
		else:
			print("Function " + function_name + " was not declared")
			sys.exit(0)

	"""
	Verifica si un atributo existe en el objeto atts
	"""
	def isAttribute(self, id):
		if id not in self.attributes.keys():
			print("Attribute " + id + " not declared in class " + self.name)
			sys.exit(0)

	"""
	Regresa la tabla de metodos
	"""
	def getMethodTable(self, function_name):
		return self.methods.getDirectory()[function_name]

	"""
	Actualiza los metodos
	"""
	def updateMethods(self, table):
		self.methods = table

	"""
	Copia los atributos de una clase a otra.
	"""
	def copyAtts(self, inherits):
		for key, value in inherits.attributes.items():
			if key in self.attributes.keys():
				print(key + " from " + inherits.getName() + " already defined in " + self.name)
				sys.exit(0)
			else:
				self.attributes[key] = value

	"""
	Copia los metodos de una clase a otra
	"""
	def copyMethods(self, inherits):
		for key, value in inherits.methods.getDirectory().items():
			if key in self.methods.getDirectory().keys():
				print(key + " from " + inherits.getName() + " already defined in " + self.name)
				sys.exit(0)
			else:
				self.methods.getDirectory()[key] = value

	"""
	Imprime la tabla de constructores
	"""
	def printConstuctorTable(self):
		for key, value in self.constructors[self.numberOfCons-1].getParameters().items():
			print("ID: " + key)
			print("Type: " + str(value.getType()))
			print("Size: " + str(value.getListSize()))
			print("Address: " + str(value.getAddress()))

	"""
	Regresa la lista que contiene a todos los parametros
	"""
	def getConstructorParams(self):
		return self.constructors

	"""
	Regresa una lista de constructores
	"""
	def getConstructorParam(self, id):
		return self.constructors[id]

	"""
	Imprime la informacion de los atributos de manera bonita
	"""
	def printAtts(self):
		for key, value in self.attributes.items():
			print("ID: " + str(key))
			print("Type: " + str(value.getType()))
			print("Accesible: " + str(value.isAccessible()))
			print("Address: " + str(value.getAddress()))

	"""
	Imprime los metodos de una manera bonita
	"""
	def printMethods(self):
		for key, value in self.methods.getDirectory().items():
			print("Function: " + key)
			print("Accessibility: " + str(value.getAccessibility()))
			print("Type: " + str(value.getReturnType()))
			for key2, value2 in value.getParamTable().getParameters().items():
				print("Var name: " + key2)
				print("Type: " + str(value2.getType()))
				print("Address: " + str(value2.getAddress()))
			for key2, value2 in value.getSymbolTable().getSymbols().items():
				print("Var name: " + key2)
				print("Type: " + str(value2.getType()))
				print("Address: " + str(value2.getAddress()))

	"""
	Imprime la informacion de la clase de manera bonita
	"""
	def printInfo(self):
		print("------------------------------------------------------")
		print("Class name: " + self.name)
		print("Inherits: " + str(self.inherits))
		self.printAtts()
		self.printMethods()
