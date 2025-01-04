class Package:
	def __init__(self, package_id, destination):
		self._package_id = package_id
		self._destination = destination

	def __str__(self):
		return (f"Package ID: {self.package_id}\n Destination: {self.destination}")

	@property
	def package_id(self):
		return self._package_id

	@property
	def destination(self):
		return self._destination

	def get_delivery_speed(self):
		return 1.5


class Perishable(Package):
	def __init__(self, package_id, destination):
			super().__init__(package_id, destination)
	def get_delivery_speed(self):
			return 1.0  
		
		
class Fragile(Package):
	def __init__(self, package_id, destination):
			super().__init__(package_id, destination)
	def get_delivery_speed(self):
			return 2.0
