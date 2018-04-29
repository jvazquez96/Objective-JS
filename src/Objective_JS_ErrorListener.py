from antlr4.error.ErrorListener import ErrorListener
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Objective_JS_ErrorListener(ErrorListener):

	def __init__(self, fileName):
		self.fileName = fileName
		super(Objective_JS_ErrorListener, self).__init__()

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		print("Syntax error: " + str(msg))
		if os.path.exists('Tests/original_copy.Objective_JS'):
			with open('Tests/original_copy.Objective_JS','r') as input, open(self.fileName, 'w+') as output:
				output.write(input.read())
		if os.path.exists('Tests/original_copy.Objective_JS'):
			os.remove('Tests/original_copy.Objective_JS')
		sys.exit()