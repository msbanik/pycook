import math
class Circle:
	def __init__(self, radius):
		self.radius = radius

	@property
	def area(self):
		return math.pi * self.radius ** 2

	@property
	def perimeter(self):
		return 2 * math.pi * self.radius


if __name__ == '__main__':
	c = Circle(10)
	print c.area
	print c.perimeter