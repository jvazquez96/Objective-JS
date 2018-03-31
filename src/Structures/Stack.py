# Clase Stack
class Stack(object):
	# Constructor de un stack vacío.
	def __init__(self):
		self.elements = []

	def empty(self):
		# Regresa True si el stack está vacío, False en caso contrario.
		return self.elements == []

	def size(self):
		# Regresa un entero indicando la cantidad de elementos en el stack.
		return len(self.elements)

	def top(self):
		# Regresa el primer elemento del stack.
		if self.size() == 0:
			return []
		else:
			return self.elements[-1]

	def push(self, element):
		# Agrega un elemento al stack.
		self.elements.append(element)

	def pop(self):
		# Elimina el último elemento del stack.
		if self.size() == 0:
			return []
		else:
			return self.elements.pop()

'''
# Declarar un stack.
my_stack = Stack()

# Agrega elementos al stack.
print("Inserting 8")
my_stack.push(8)
print("Inserting 2")
my_stack.push(2)
print("Inserting 3")
my_stack.push(3)

# Verifica si el stack esta vacío.
if my_stack.empty():
	print("The stack is empty")
else:
	print("The stack is not empty")

# Imprime el elemento al tope del stack junto con su tamaño.
print("Top: " + str(my_stack.top()))
print("Size: " + str(my_stack.size()))

# Saca el último elemento del stack.
print("Popping the last element of the stack")
my_stack.pop()

# Imprime el elemento al tope del stack junto con su tamaño.
print("Top: " + str(my_stack.top()))
print("Size: " + str(my_stack.size()))

# Saca el último elemento del stack
print("Popping the last element of the stack")
my_stack.pop()

# Imprime el elemento al tope del stack junto con su tamaño.
print("Top: " + str(my_stack.top()))
print("Size: " + str(my_stack.size()))

# Saca el último elemento del stack
print("Popping the last element of the stack")
my_stack.pop()

# Imprime el elemento al tope del stack junto con su tamaño.
print("Top: " + str(my_stack.top()))
print("Size: " + str(my_stack.size()))

# Verifica si el stack esta vacío.
if my_stack.empty():
	print("The stack is empty")
else:
	print("The stack is not empty")
'''