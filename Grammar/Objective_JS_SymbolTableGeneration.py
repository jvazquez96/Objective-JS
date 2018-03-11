import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSListener import Objective_JSListener
from SymbolTable import SymbolTable
from InfoDirectory import InfoDirectory
from FunctionsDirectory import FunctionsDirectory

class Objective_JS_SymbolTableGeneration(Objective_JSListener):

	def __init__(self):
		self.functions_directory = FunctionsDirectory()
		self.type = None
		# Default visibility
		self.visibility = "private"
		self.does_returns = None
		self.function_name = None

	def getFunctionDirectory(self):
		return self.functions_directory

	def getSymbolsTables(self):
		return self.functions_directory.getDirectory()

	def newClass(self, className):
		self.function_name = className
		self.functions_directory.create_table(self.function_name, InfoDirectory())

	def newVars(self, id, type, visibility):
		if id in self.functions_directory.getSymbolTable(self.function_name).getTable():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		self.functions_directory.getSymbolTable(self.function_name).push_frame(id, type, visibility)

	def newFunction(self):
		if self.function_name not in self.functions_directory.getDirectory():
			self.functions_directory.create_table(self.function_name, InfoDirectory(SymbolTable(), self.does_returns))
		else:
			print("Syntax error!! Function: " + self.function_name + " is already defined")
			sys.exit(0)
			

	def enterVars_(self, ctx):
		id = ctx.ID().getText()
		self.type = ctx.tipo_dato().getText()
		self.newVars(id, self.type, self.visibility)

	def enterClase(self, ctx):
		className = ctx.CLASSNAME().getText()
		self.newClass(className)

	def enterVarsAux(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.newVars(id, self.type, self.visibility)

	def enterVarsRepeated(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.type = ctx.tipo_dato().getText()
			self.newVars(id, self.type, self.visibility)

	def enterAtributosPublic(self, ctx):
		self.visibility = ctx.PUBLIC().getText()

	def enterAtributosPrivate(self, ctx):
		self.visibility = ctx.PRIVATE().getText()

	def enterImpFunc(self, ctx):
		if ctx.FUNCTION() is not None:
			self.function_name = ctx.ID().getText()

	def enterImpFuncAux2(self, ctx):
		if ctx.RETURNS() is None:
			self.does_returns = None
		else:
			self.does_returns = "returns"
		self.newFunction()

	def enterClass_declaration(self, ctx):
		self.function_name = ctx.CLASSNAME().getText()
		self.functions_directory.create_table(self.function_name, InfoDirectory())

	def enterMain_header(self, ctx):
		self.function_name = "main"
		self.functions_directory.create_table("main", InfoDirectory())

	def exitBloqueFuncAux2(self, ctx):
		self.functions_directory.remove_info(self.function_name)
		self.function_name = None
