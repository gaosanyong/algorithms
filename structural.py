"""STRUCTURAL DESIGN PATTERNS
- decorator
- proxy
- adapter
- composite
- bridge
"""

"""DECORATOR
PROBLEM: 
* new features to an existing object
* dynamic changes
* not using subclassing
SCENARIO:
* Hello World! <blink>Hello World!</blink>
SOLUTION:
* functions are objects in Python
* built-in decorator feature
RELATED PATTERNS:
* adaptor
* composite
* strategy
"""

from functools import wraps

def make_blink(function):
	"""Defines the decorator"""
	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator

#Apply the decorator here!
@make_blink
def hello_world():
	"""Original function!"""
	return "Hello, World!"

# #Check the result of decorating
# print(hello_world())

# #Check if the function name is still the name of the function being decorated
# print(hello_world.__name__)

# #Check if the docstring is still the same as that of the 
# print(hello_world.__doc__)

"""PROXY
PROBLEM 
* postpone object cfreation unless absolutely necessary
* find a placeholder
SCENARIO
* producer
* artist (proxy)
* guest
SOLUTION
clients -- interacting with a proxy 
proxy -- responsible for creating the resoruce intensive object 
RELAT3ED PATTERN
* adapter 
* decorator 
"""

import time

class Producer: 
	"""Define the 'resource-intensive' object in instantiate!"""
	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")

class Proxy:
	"""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
	def __init__(self):
		self.occupied = "No"
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")
		if self.occupied == 'No':
			#If the producer is available, create a producer object!
			self.producer = Producer()
			time.sleep(2)

			#Make the producer meet the guest!
			self.producer.meet()

		else:
			#Otherwise, don't instantiat a producer
			time.sleep(2)
			print("Producer is busy!")

# #Instantiate a Proxy
# p = Proxy()

# #Make the proxy: Artist produce untile Producer is available
# p.produce()

# #Change the state of 'occupied'
# p.occupied = 'Yes'

# #Make the Producer produce
# p.produce()

"""ADAPTER
PROBLEM
* incompatible interface
SENARIO
* korean -- speak_korean 
* british -- speak_english
* client -- speak 
SOLUTION
* translation
RELATED PATTERNS
* bridges 
* decorator 
"""
class Korean:
	"""Korean speaker"""
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "An-neyong?"


class British:
	"""English speaker"""
	def __init__(self):
		self.name = "British"

	#Note the different method name here!
	def speak_english(self):
		return "Hello!"


class Adapter:
	"""This changes the generic method name to individualized method names"""
	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object = object
		#add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_korean() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply return the rest of attributes!"""
		return getattr(self._object, attr)

# #List to store speaker objects
# objects = []

# #Create a Korean object
# korean = Korean()

# #Create a British object
# british = British()

# #Append the objects to the object list
# objects.append(Adapter(korean, speak=korean.speak_korean))
# objects.append(Adapter(british, speak=british.speak_english))

# for obj in objects:
# 	print("{} says '{}'".format(obj.name, obj.speak()))

"""COMPOSITE
PROBLEM
* recrusive tree data structure
* menu > submenu > sub-submenu > ...
SCENARIO 
* menu
* submenu
SOLUTION
* component
* child
* composite
RELATED PATTERNS
* decorator 
* iterator 
* visitor
"""

class Component(object):
	"""Abstract class"""
	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): #Inherits from the abstract class, Component
	"""Concrete class"""
	def __init__(self, *args, **kwargs):
		super(Child, self).__init__(*args, **kwargs)
		
		#This is where we store the name of your child item!
		self.name = args[0]

	def component_function(self):
		#Print the name of your child item here!
		print(f"{self.name}")		

class Composite(Component): #Inherits from the abstract class, Component
	"""Concrete class and maintains the tree recursive structure"""

	def __init__(self, *args, **kwargs):
		super(Composite, self).__init__(*args, **kwargs)

		#This is where we store the name of the composite object
		self.name = args[0]

		#This is where we keep our child items
		self.children = []

	def append_child(self, child):
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove a child item"""
		self.children.remove(child)

	def component_function(self):
		#Print the name of the composite object
		print(f"{self.name}")

		#Iterate through the child objects and invoke their component function printing their names
		for i in self.children:
			i.component_function()

# #Build a composite submenu 1
# sub1 = Composite("Submenu1")

# #Create a new child sub_submenu 11
# sub11 = Child("sub_submenu 11")
# #Create a new Child sub_submenu 12
# sub12 = Child("sub_submenu 12")

# #Add the sub_submenu 11 to submenu 1
# sub1.append_child(sub11)
# #Add the sub_submenu 12 to submenu 1
# sub1.append_child(sub12)

# #Build a top-level composite menu
# top = Composite("top_menu")

# #Build a submenu 2 that is not a composite 
# sub2 = Child("submenu2")

# #Add the composite submenu 1 to the top-level composite menu
# top.append_child(sub1)

# #Add the plain submenu 2 tot he top-level composite menu
# top.append_child(sub2)

# #Let's test if our Composite pattern works!
# top.component_function()

"""BRIDGE
PROBLEM 
* two unrelated, parallel or orthogonal abstractions
* one -- implementation specific 
* the other -- implementation independent 
SCENARIO 
* implementation-independent circle abstraction
* implementation-dependent circle abstraction
SOLUTION
* separate the abstrations into two different class hierarchies
RELATED PATTERNS
* abstract factory 
* adaptor
"""
class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print(f"API 1 drawing a circle at ({x}, {y} with {radius}!)")

class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x, y, radius):
		print(f"API 2 drawing a circle at ({x}, {y} with {radius}!)")
								
class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""
	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api
	
	def draw(self):
		"""IMplementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		self._radius *= percent

#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Buidl the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
#Draw a circle
circle2.draw()