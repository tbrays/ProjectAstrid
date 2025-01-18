"""
interface.py

Provides the `Interface` class to manage user interactions with a humanoid 
robot system via a command-line interface (CLI).

Features:
- Displays boot messages, menus and maps.
- Handles user input for robot operations.
- Manages a delivery menu for department selection.
- Displays error messages for invalid inputs.
- Supports shutdown with user confirmation.

Classes:
    Environment: Encapsulates the map and provides utilities for robot navigation.
"""


import sys
from utils import clear_console


class Interface:
    """
    Interface class for managing user interactions with the humanoid robot system.

    This class provides methods for displaying menus, maps and handling user inputs
    to control the robot's operations.
    """

    def __init__(self):
        """
        Initialise the Interface with menu options.
        """
        self._menu_options = {
            1: "Display Map",
            2: "Delivery",
            3: "Shutdown"
        }

    @property
    def menu_options(self):
        """
        Get the available menu options.

        Returns:
            dict: A dictionary of menu options.
        """
        return self._menu_options

    def boot(self, name, model, manufacturer):
        """
        Display the boot screen with robot information.

        Args:
            name (str): Name of the robot.
            model (str): Model of the robot.
            manufacturer (str): Manufacturer of the robot.
        """
        clear_console()
        print("=" * 50)
        print("\033[1;37;44m                     Welcome                      \033[0m")
        print("=" * 50)
        print(f"\033[1;35m               My name is {name},")
        print(f"\033[1;35m    I am an {model}, manufactured by {manufacturer}.    \033[0m")
        print(r"""
                     ╔╩════╩╗
                    ╔╣ █  █ ╠╗
                    ╚╣\____/╠╝
                     ╚══════╝
        """)
        print("\033[1;35m  A Highly Intelligent Automated Delivery System    \033[0m")
        print("\n\033[1;33m  Booting up...\033[0m")
        print("=" * 50)
        input("Press Enter to continue to the main menu...")

    def display_menu(self, name):
        """
        Display the main menu and handle user input.

        Args:
            name (str): Name of the robot.

        Returns:
            int: User's menu choice.
        """
        while True:
            clear_console()
            print("=" * 50)
            print(f"\033[1;37;42m           {name} - Main Control Panel            \033[0m")
            print("=" * 50)

            for option, description in self.menu_options.items():
                print(f"\033[34m{option}. {description}\033[0m")

            print("=" * 50)

            try:
                prompt = f"\033[1;33mPlease select an option (1-{len(self.menu_options)}): \033[0m"
                choice = int(input(prompt))
                if choice in self.menu_options:
                    return choice

                self.display_invalid_choice_message()
            except ValueError:
                self.display_invalid_choice_message()

    def display_map(self, map_str):
        """
        Display the current map of the environment.

        Args:
            map_str (str): String representation of the map.
        """
        clear_console()
        print("=" * 50)
        print("\033[1;37;42m             Moon Base Luna-9 Map                 \033[0m")
        print("=" * 50)
        print(map_str)
        print("=" * 50)

    def display_delivery_menu(self):
        """
        Display the delivery menu and handle user input.

        Returns:
            str: Selected department name.
        """
        departments = {
            1: "Engineering",
            2: "Command",
            3: "Medical Bay",
            4: "Airlock",
            5: "Hydroponics",
            6: "Cargo",
            7: "Docking"
        }

        while True:
            clear_console()
            print("=" * 50)
            print("\033[1;37;42m                   Delivery Menu                  \033[0m")
            print("=" * 50)
            print("\033[1;33mSelect a department for the delivery job:\033[0m")

            for num, dept_name in departments.items():
                print(f"\033[34m{num}. {dept_name}\033[0m")

            print("=" * 50)

            try:
                choice = int(input("\033[1;33mPlease select a department (1-7): \033[0m"))
                if choice in departments:
                    return departments[choice]

                print("\033[1;31mInvalid choice! Please select a valid department.\033[0m")
                input("Press Enter to try again...")
            except ValueError:
                print("\033[1;31mInvalid input! Please enter a number between 1 and 7.\033[0m")
                input("Press Enter to try again...")

    def display_invalid_choice_message(self):
        """
        Display an invalid choice message to the user.
        """
        print(
            f"\033[1;31mInvalid choice! Please enter a number between "
            f"1 and {len(self.menu_options)}.\033[0m"
        )
        input("Press Enter to try again...")

    def shutdown(self):
        """
        Handle the shutdown sequence, confirming with the user.

        If the user confirms, the program exits. Otherwise, returns to the menu.
        """
        confirmation = input("\033[1;31mAre you sure you want to shut down? (y/n): \033[0m").lower()
        if confirmation == 'y':
            print("\033[1;31mShutting down... Goodnight\033[0m")
            sys.exit()
        else:
            print("\033[1;32mShutdown cancelled. Returning to the main menu.\033[0m")
            input("Press Enter to return to the menu...")
