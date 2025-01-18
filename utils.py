"""
Utility Module

This module provides utility functions for the robot delivery system, including 
functions to clear the console screen and generate a random package ID.

Functions:
    clear_console: Clears the terminal or console screen.
    generate_id: Generates a random integer between 10 and 250 as a package ID.
"""

import os
import random


def clear_console():
    """
    Clears the console screen.

    This function clears the console based on the operating system being used:
    - For Windows, it uses the `cls` command.
    - For other operating systems, it uses the `clear` command.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def generate_id():
    """
    Generates a random package ID.

    Returns:
        int: A random integer between 10 and 250 to be used as a package ID.
    """
    return random.randint(10, 250)
