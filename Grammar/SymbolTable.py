import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSListener import Objective_JSListener

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
	def test(self):
		print(1)