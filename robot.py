"""
Robot Delivery System Module

This module defines the `Robot` class, which represents a humanoid robot responsible 
for delivering packages on a space station. It interacts with the environment, manages 
an inventory of packages, and uses an interface to display menus, maps and delivery status.

Features:
- Robot's name, model and manufacturer are provided during initialisation.
- The robot can navigate the station to deliver packages to different departments.
- Pathfinding using Breadth-First Search (BFS) for determining the shortest path.
- Inventory management for storing packages (supports Perishable, Fragile, and generic packages).
- A user interface to display the map and delivery menu options.
- A simulation of delivery speed for different types of packages.

Classes:
    Robot: Represents the humanoid robot with delivery capabilities.
"""


import time
from interface import Interface
from package import Package, Perishable, Fragile
from utils import generate_id


class Robot:
    """
    Represents a humanoid robot for package delivery.

    Attributes:
        name (str): The name of the robot.
        model (str): The robot's model identifier.
        manufacturer (str): The manufacturer of the robot.
        position (tuple): The current (row, col) position of the robot.
        inventory (list): List of packages currently held by the robot.
        environment (Environment): The environment where the robot operates.
        interface (Interface): User interface for interacting with the robot.
    """

    def __init__(self, name, model, manufacturer, environment):
        """
        Initialise the robot with basic details and its operating environment.

        Args:
            name (str): The name of the robot.
            model (str): The model identifier of the robot.
            manufacturer (str): The manufacturer of the robot.
            environment (Environment): The operating environment of the robot.
        """
        self._name = name
        self._model = model
        self._manufacturer = manufacturer
        self.position = (6, 0)
        self.inventory = []
        self.environment = environment
        self.interface = Interface()

    @property
    def name(self):
        """Get the robot's name."""
        return self._name

    @property
    def manufacturer(self):
        """Get the robot's manufacturer."""
        return self._manufacturer

    @property
    def model(self):
        """Get the robot's model."""
        return self._model

    def __str__(self):
        """
        String representation of the robot, including its name, model and manufacturer.

        Returns:
            str: A description of the robot.
        """
        return (
            f"My Name is {self.name}, I am an {self.model} made by {self.manufacturer}."
            "\nMy job is to deliver packages on the space station."
        )

    def start_up(self):
        """
        Start up the robot and display the main menu.

        Continuously handle user interactions until shutdown.
        """
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
        """
        Handle the delivery process, including package creation and navigation.

        The robot selects a department, creates a package and navigates to the destination.
        """
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
