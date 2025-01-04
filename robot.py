from interface import Interface
from package import Package, Perishable, Fragile
from utils import generate_id
import time

class Robot:
	def __init__(self, name, model, manufacturer, environment):
		self._name = name
		self._model = model
		self._manufacturer = manufacturer
		self.position = (6, 0)
		self.inventory = []
		self.environment = environment
		self.interface = Interface()

	@property
	def name(self):
		return self._name

	@property
	def manufacturer(self):
		return self._manufacturer

	@property
	def model(self):
		return self._model

	def __str__(self):
		return (
			f"My Name is {self.name}, I am an {self.model} made by {self.manufacturer}"
			"\nMy job is to deliver packages on the space station"
		)

	def start_up(self):
		self.interface.boot(self.name, self.model, self.manufacturer)

		while True:
			user_choice = self.interface.display_menu(self.name)

			if user_choice == 1:
				self.interface.display_map(self.environment.generate_map(self.position))
				input("Press Enter to return to the main menu...")
			elif user_choice == 2:
				self.delivery()
			elif user_choice == 3:
				self.interface.shutdown()

	def delivery(self):
		department = self.interface.display_delivery_menu()
		
		if department:
			package_id = generate_id()

			if department == "Medical Bay":
				package = Perishable(package_id, department)
			elif department == "Airlock":
				package = Fragile(package_id, department)
			else: 
				package = Package(package_id, department)

			self.inventory.append(package)
			
			path = self.environment.find_path(self.position, self.inventory[0].destination)

		if path:
			for step in path:
				self.position = step
				map_str = self.environment.generate_map(self.position) 
				self.interface.display_map(map_str)  
				delivery_speed = self.inventory[0].get_delivery_speed()
				time.sleep(delivery_speed)		
		else:
			print("No path found.")

		self.inventory.clear()
		print("Delivery complete!")
		input("Press Enter to return to the main menu...")
