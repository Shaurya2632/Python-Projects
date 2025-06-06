
class Vector:

	def __init__(self, i, j, k):

		self.i = i
		self.j = j
		self.k = k

	def __str__(self):

		return f"{self.i, self.j, self.k}"

	def __add__(self, vector):

		return Vector(self.i + vector.i, self.j + vector.j, self.k + vector.k)

	def __sub__(self, vector):

		return Vector(self.i - vector.i, self.j - vector.j, self.k - vector.k)

	def __mul__(self, vector):

		return Vector(self.i * vector.i, self.j * vector.j, self.k * vector.k)

	def __truediv__(self, vector):

		return Vector(self.i / vector.i, self.j / vector.j, self.k / vector.k)

	def __eq__(self, vector):

		return self.__dict__ == self.__dict__

	def __format__(self, format_spec):

		match format_spec:

			case ".2f": return f"({self.i:.2f}, {self.j:.2f}, {self.k:.2f})"

		return None

v1 = Vector(13, 65, 43)
v2 = Vector(83, 31, 53)

print(v2 - v1)


