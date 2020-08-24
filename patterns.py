"""DESIGN PATTERN 

Design patterns are repeatable solutions to commonly occurring problems in 
software design. 

  category | language     | purpose 
-----------------------------------------------
creational | polymorphism | object creation
structural | inheritance  | object relationship
behavioral | methods      | object interaction
-----------------------------------------------

creational       | structural | behavioral
-------------------------------------------------------
abstract factory | adapter    | chain of responsibility
builder          | bridge     | command
factory method   | composite  | interpreter
prototype        | decorator  | iterator
singleton        | facade     | mediator
                 | flyweight  | memento
                 | proxy      | observer
                 |            | state
                 |            | strategy
                 |            | template method
                 |            | visitor 
-------------------------------------------------------              

class -- template to create objects (attributes & methods)

PATTERN CONTEXT
* participants -- classes 
* quality attributes -- nonfunctional requirements 
* forces -- factors / trade-offs 
* consequences -- side effects & decision makers 	
"""

"""FACTORY
uncertainties in types of objects
decision to be made at runtime regarding what classes to use 
"""
class Dog: 
	"""A simnple dog class"""
	def __init__(self, name):
		self._name = name 

	def speak(self):
		return "Woof!"

	def __str__(self):
		return str(self._name)

class Cat: 
	"""A simnple dog class"""
	def __init__(self, name):
		self._name = name 

	def speak(self):
		return "Meow!"

	def __str__(self):
		return str(self.name)


def get_pet(pet="dog"):
	"""The factory method"""
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
	return pets[pet]

# dog = get_pet("dog")
# print(dog.speak())

# cat = get_pet("cat")
# print(cat.speak())


"""ABSTRACT FACTORY
the user expectation yields multiple related objects 

abstract factory | pet factory
concrete factory | dog factory => dog food
                 | cat factory => cat food 
abstract product |
concrete product | dog food & cat food                   
"""
class DogFactory:
	"""Concrete Factory"""
	def get_pet(self):
		"""Rturn a Dog object"""
		return Dog("Fido")

	def get_food(self):
		"""Return a Dog Food objects"""
		return "Doog Food!"

class PetStore:
	"""PetStore houses our Abstract Factory"""
	def __init__(self, pet_factory=None):
		"""pet_factory is our Abstract Factory"""
		self._pet_factory = pet_factory

	def show_pet(self):
		"""Utility method to display the details of the objects returned by the DogFactory"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'".format(pet_food))

# #Create a Concrete Factory
# factory = DogFactory()

# #Create a pet store housing our Abstract Factory
# shop = PetStore(factory)

# #Invoke the utility method to show the details of our pet
# shop.show_pet()


"""SINGTON -- OOP way of creating global variable"""
#Borg design pattern

class Borg:
	"""Borg class amking class attributes global"""
	_shared_state = {} #Attribute dictionary

	def __init__(self):
		self.__dict__ = self._shared_state #Make it an attribute dictionary


class Singleton(Borg):
	"""This class now shares all its attributes among its variaous instances"""
	#This essentially makes the singleton objects an object-oriented global variable

	def __init__(self, **kwargs):
		Borg.__init__(self)
		#Update the attribute dictionary by inserting a new key-value pair
		self._shared_state.update(kwargs)

	def __str__(self):
		#Returns the attribute dictionary for printing 
		return str(self._shared_state)

# #Let's create a singleton object and add our first acronym
# x = Singleton(HTTP = "Hyper Text Transfer Protocol")
# #Print the object
# print(x)
# #Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
# y = Singleton(SNMP = "Simple Network Management Protocol")
# #Print the object 
# print(y)

"""BUILDER PATTERN <==> telescoping constructor anti-pattern
* directory
* abstract builder -- defines interfaces
* concrete builder -- implements interfaces
* object 
"""
class Director():
	"""Director"""
	def __init__(self, builder):
		self._builder = builder
	
	def construct_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tires()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car


class Builder():
	"""Abstract Builder"""
	def __init__(self):
		self.car = None

	def create_new_car(self):
		self.car = Car()


class SkyLarkBuilder(Builder):
	"""Concrete Builder --> provides parts and tools to work on the parts"""
	def add_model(self):
		self.car.model = "Skylark"

	def add_tires(self):
		self.car.tires = "Regular tires"

	def add_engine(self):
		self.car.engine = "Turbo engine"
		

class Car():
	"""Product"""
	def __init__(self):
		self.model = None
		self.tires = None
		self.engine = None

	def	__str__(self):
		return '{} | {} | {}'.format(self.model, self.tires, self.engine)


# builder = SkyLarkBuilder()
# director = Director(builder)
# director.construct_car()
# car = director.get_car()
# print(car)

"""PROTOTYPE
creating many identical objects individually - expensive
mass production
create a prototypical instance first
simply clone it whenever you need replica
"""

import copy 

class Prototype:

	def __init__(self):
		self._objects = {}

	def register_object(self, name, obj):
		"""Register an object"""
		self._objects[name] = obj

	def unregister_object(self, name):
		"""Unregister an object"""
		del self._objects[name]

	def clone(self, name, **attr):
		"""Clone a registered object and update its attributes"""
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj


class Car:
	def __init__(self):
		self.name = "Skylark"
		self.color = "Red"
		self.options = "Ex"

	def __str__(self):
		return '{} | {} | {}'.format(self.name, self.color, self.options)

car = Car() #prototypical object to be replicated
prototype = Prototype()
prototype.register_object("skylark", car)
car1 = prototype.clone("skylark")
print(car1)