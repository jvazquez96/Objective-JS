import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSVisitor import Objective_JSVisitor

class SymbolTable(object):
	def __init__(self):
		self._symbols = dict()
	def push_frame(self, id, type=None, attribute=None):
		if type is not None and attribute is not None:
			self._symbols[id] = Info(type, attribute);
		else:
			content = Info(type, attribute)
			self._symbols[id] = content
	def remove_frame(self, id):
		self._symbols[id]
	def size(self):
		return len(self._symbols)
	def getContent(self, id):
		if id in self._symbols:
			return self._symbols[id]
		else:
			return []
	def getTable(self):
		return self._symbols


# test = SymbolTable()
# test.push_frame('a', 'int', 'private')
# test.push_frame('b', 'int', 'public')
# print(test.size())
# print(test.getContent('a').getType())
# print(test.getContent('b').getVisibility())
# test.remove_frame('a')
# print(test.size())

class SemanticAnalysis(Objective_JSVisitor):

	def __init__(self):
		self.symbols = SymbolTable()

	def getSymbolsTable(self):
		return self.symbols.getTable()

	def newClass(self, className):
		self.symbols.push_frame(className)

	def newVars(self, id, type, visibility):
		self.symbols.push_frame(id, type, visibility)

	def visitClase(self, ctx):
		className = ctx.CLASSNAME().getText()
		self.newClass(className)

	def visitVars_(self, ctx):
		id = ctx.ID().getText()
		type = ctx.tipo_dato().getText()
		self.newVars(id, type, "protected")

	def visitClaseAux(self, ctx):
		pass

	def visitBloqueClase(self, ctx):
		pass

	




if __name__ == '__main__':
    inputs  = FileStream(sys.argv[1])
    lexer   = Objective_JSLexer(inputs)
    tokens  = CommonTokenStream(lexer)
    parser  = Objective_JSParser(tokens)
    tree    = parser.inicio()
    codegen = SemanticAnalysis()
    codegen.visit(tree)
    for key, value in codegen.getSymbolsTable().items():
    	print("Key: " + str(key))
    	print("Value: " + str(value))
