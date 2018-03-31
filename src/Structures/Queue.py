# Clase Queue
class Queue(object):
	# Constructor de una queue vacía.
	def __init__(self):
		self.elements = []

	def empty(self):
		# Regresa True si la queue esta vacía, False en caso contrario.
		return self.elements == []

	def size(self):
		# Regresa un entero indicando la cantidad de elementos en la queue.
		return len(self.elements)

	def front(self):
		# Regresa el primer elemento de la queue.
		if self.size() == 0:
			return []
		else:
			return self.elements[0]

	def back(self):
		# Regresa el último elemento de la queue.
		if self.size() == 0:
			return []
		else:
			return self.elements[-1]

	def push(self, element):
		# Agrega un elemento a la queue.
		self.elements.append(element)

	def pop(self):
		# Elimina el último elemento de la queue.
		if self.size() == 0:
			return []
		else:
			return self.elements.pop(0)

'''
# Declarar una queue.
my_queue = Queue()

# Agrega elementos a la queue.
print("Inserting 8")
my_queue.push(8)
print("Inserting 2")
my_queue.push(2)
print("Inserting 3")
my_queue.push(3)

# Verifica si la queue esta vacía.
if my_queue.empty():
	print("The queue is empty")
else:
	print("The queue is not empty")

# Imprime el elemento al frente, al final y el tamaño de la queue.
print("front: " + str(my_queue.front()))
print("back: " + str(my_queue.back()))
print("Size: " + str(my_queue.size()))

# Saca el primer elemento de la queue.
print("Popping the first element of the queue")
my_queue.pop()

# Imprime el elemento al frente, al final y el tamaño de la queue.
print("front: " + str(my_queue.front()))
print("back: " + str(my_queue.back()))
print("Size: " + str(my_queue.size()))

# Saca el primer elemento de la queue.
print("Popping the first element of the stack")
my_queue.pop()

# Imprime el elemento al frente, al final y el tamaño de la queue.
print("front: " + str(my_queue.front()))
print("back: " + str(my_queue.back()))
print("Size: " + str(my_queue.size()))

# Saca el primer elemento de la queue.
print("Popping the first element of the stack")
my_queue.pop()

# Imprime el elemento al frente, al final y el tamaño de la queue.
print("front: " + str(my_queue.front()))
print("back: " + str(my_queue.back()))
print("Size: " + str(my_queue.size()))

# Verifica si la queue esta vacía.
if my_queue.empty():
	print("The queue is empty")
else:
	print("The queue is not empty")
'''