#!/usr/bin/python3

class Hello():
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def print_message(self):
		for i in range(10):
			print("Hello World" + str(i))

if __name__ == '__main__':
	h = Hello()
	h.print_message()
