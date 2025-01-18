"""
Package Module

This module defines the `Package` class and its specialised subclasses, `Perishable` 
and `Fragile`. These classes represent different types of packages handled by the robot 
for delivery on a space station.

Features:
- Class represents a general package with a unique ID and destination.
- Subclass represents packages that require faster delivery.
- Subclass represents packages that require slower and more careful delivery.
- Each class provides a method to simulate delivery speed for different types of packages.
- Class includes attributes for the package ID and destination, which are used for 
	identifying and routing packages to their destinations.

Classes:
    Package: Represents a general package with a unique ID and destination.
    Perishable: Represents a perishable package with faster delivery requirements.
    Fragile: Represents a fragile package with slower delivery requirements.
"""


class Package:
    """
    Represents a general package with a unique ID and destination.

    Attributes:
        package_id (str): The unique identifier of the package.
        destination (str): The destination department of the package.
    """

    def __init__(self, package_id, destination):
        """
        Initialise the package with its ID and destination.

        Args:
            package_id (str): Unique identifier for the package.
            destination (str): Destination department for the package.
        """
        self._package_id = package_id
        self._destination = destination

    def __str__(self):
        """
        String representation of the package.

        Returns:
            str: A string displaying the package ID and destination.
        """
        return f"Package ID: {self.package_id}\nDestination: {self.destination}"

    @property
    def package_id(self):
        """
        Get the package's unique identifier.

        Returns:
            str: The unique ID of the package.
        """
        return self._package_id

    @property
    def destination(self):
        """
        Get the package's destination.

        Returns:
            str: The destination department of the package.
        """
        return self._destination

    def get_delivery_speed(self):
        """
        Get the delivery speed for the package.

        Returns:
            float: The delivery speed in seconds per step.
        """
        return 1.5


class Perishable(Package):
    """
    Represents a perishable package that requires faster delivery.

    Inherits from:
        Package
    """

    def __init__(self, package_id, destination):
        """
        Initialise the perishable package with its ID and destination.

        Args:
            package_id (str): Unique identifier for the package.
            destination (str): Destination department for the package.
        """
        super().__init__(package_id, destination)

    def get_delivery_speed(self):
        """
        Get the delivery speed for the perishable package.

        Returns:
            float: Faster delivery speed in seconds per step.
        """
        return 1.0


class Fragile(Package):
    """
    Represents a fragile package that requires careful and slower delivery.

    Inherits from:
        Package
    """

    def __init__(self, package_id, destination):
        """
        Initialise the fragile package with its ID and destination.

        Args:
            package_id (str): Unique identifier for the package.
            destination (str): Destination department for the package.
        """
        super().__init__(package_id, destination)

    def get_delivery_speed(self):
        """
        Get the delivery speed for the fragile package.

        Returns:
            float: Slower delivery speed in seconds per step.
        """
        return 2.0
