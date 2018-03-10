import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSListener import Objective_JSListener
from SymbolTable import SymbolTable

class Objective_JS_SymbolTableGeneration(Objective_JSListener):

	def __init__(self):
		self.symbols = SymbolTable()
		self.type = None
		# Default visibility
		self.visibility = "private"

	def getSymbolsTable(self):
		return self.symbols.getTable()

	def newClass(self, className):
		self.symbols.push_frame(className)

	def newVars(self, id, type, visibility):
		if id in self.symbols.getTable():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		self.symbols.push_frame(id, type, visibility)

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
