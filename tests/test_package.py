import pytest
from package import Package, Perishable, Fragile

def test_package_initialisation():
		package = Package(package_id="123", destination="Medical Bay")
		assert package.package_id == "123"
		assert package.destination == "Medical Bay"

def test_perishable_package_speed():
		package = Perishable(package_id="124", destination="Medical Bay")
		assert package.get_delivery_speed() == 1.0

def test_fragile_package_speed():
		package = Fragile(package_id="125", destination="Airlock")
		assert package.get_delivery_speed() == 2.0
