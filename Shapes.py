from abc import ABC, abstractmethod
class Shape(ABC):
	@abstractmethod
	
	def area(self):
		pass
	
	@abstractmethod
		
	def perimeter(self):
		pass
		
class Circle (Shape):
	def __init__(self,radius):
		self.radius = radius
		
	def area (self):
		return 3.14 *self.radius * self.radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius * self.radius
			
class Rectangle (Shape):
	def __init__(self,length,width):
		self.length = length
		self.width = width
		
	def perimeter(self):
		return 2 * (self.length + self.width)
		
	def area (self):
		return 2 * self.length * self.width
		
class Triangle(Shape):
		def __init__(self,base,height,side1,side2,side3):
			self.base = base
			self.height = height
			self.side1 = side1
			self.side2 = side2
			self.side3 = side3
		def area(self):
			return 1/2 * self.base * self.height 
			
		def perimeter(self):
			return self.side1 + self.side2 + self.side3
		
		
c = Circle(3)
r = Rectangle(4,5)
t = Triangle(8,9,3,5,7)
print(round(c.area(),2))
print(round(c.perimeter(),2))
print(r.area())
print(r.perimeter())
print(round(t.area(),2))
print(t.perimeter())

shapes = [Circle(3), Rectangle(4, 5), Triangle(8,9,3,5,7)]
for shape in shapes:
    print(type(shape).__name__, shape.area(), shape.perimeter())

