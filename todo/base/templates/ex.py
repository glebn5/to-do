class Tree:
	def __init__(self, title: str ):
		self.__title = title
		self.age = 0
		self.height = 0

	def set_title(self, title: str):
		self.__title = title
	
	def get_title(self) -> str:
		return self.__title
	
	title = property(get_title, set_title)

	def birthday(self, age: int):
		self.age += age

	def growing(self, height: int):
		self.height += height

	def about_tree(self) -> str:
		print(f'Дерево {self.get_title()}, возрастом {self.age}, ростом {self.height} см.')

