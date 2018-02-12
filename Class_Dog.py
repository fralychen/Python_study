class Dog:
	
	def __init__(self,name):
		self.name = name
		self.tricks = []

	def add_trick(self,trick):
		self.tricks.append(trick)


'''
	import Class_Dog
	d = Class_Dog.Dog('Fibo')
	e = Class_Dog.Dog('Buddy')
	d.add_trick('roll over')
	e.add_tricl('play dead')


	d.tricks
		['roll over']
	e.tricks
		['play dead']
'''
