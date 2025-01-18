"""
environment.py

This module defines the Environment class, which represents the operational 
environment for a robot. The Environment class provides functionality to 
represent the map, validate positions, find paths and generate a visual 
representation of the environment.

Features:
- A predefined map layout with various departments and obstacles.
- Methods to check the validity of positions on the map.
- Pathfinding using Breadth-First Search (BFS) for navigating the map.
- A method to generate a coloured, string-based representation of the map, 
  including the robot's position.

Classes:
    Environment: Encapsulates the map and provides utilities for robot navigation.
"""


class Environment:
    """
    Represents the environment where the robot operates.

    Provides a map of the environment, validates positions, finds paths
    using BFS and generates a visual representation of the map.
    """

    def __init__(self):
        """
        Initialise the environment with a predefined map and dimensions.
        """
        self._map = [
            ['X', 'X', 'X', 'X', 'X', 'E', 'X'],
            ['X', 'X', '.', '.', '.', '.', 'X'],
            ['X', 'X', '.', 'X', 'X', '.', 'X'],
            ['X', '.', '.', 'C', 'X', '.', 'X'],
            ['X', 'M', '.', '.', '.', '.', 'A'],
            ['X', '.', '.', '.', 'X', '.', 'X'],
            ['.', '.', 'X', 'H', 'X', 'D', 'X'],
            ['G', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

        self.rows = len(self.map)
        self.cols = len(self.map[0])

    @property
    def map(self):
        """
        Get the environment map.

        Returns:
            list: 2D list representing the map.
        """
        return self._map

    def is_valid_position(self, row, col):
        """
        Check if a position is valid and not an obstacle.

        Args:
            row (int): Row index of the position.
            col (int): Column index of the position.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols and self.map[row][col] != 'X'

    def find_path(self, start_position, destination):
        """
        Find the shortest path from a start position to a destination.

        Uses Breadth-First Search (BFS) to determine the path.

        Args:
            start_position (tuple): Starting coordinates (row, col).
            destination (str): Target destination character.

        Returns:
            list: List of coordinates representing the path, or None if no path exists.
        """
        queue = [start_position]
        visited = set()
        visited.add(start_position)
        previous = {start_position: None}

        while queue:
            current = queue.pop(0)
            row, col = current

            if self.map[row][col].upper() == destination[0].upper():
                path = []
                while current:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                return path

            for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + move[0], col + move[1]
                new_position = (new_row, new_col)

                if self.is_valid_position(new_row, new_col) and new_position not in visited:
                    queue.append(new_position)
                    visited.add(new_position)
                    previous[new_position] = current

        return None

    def generate_map(self, robot_position):
        """
        Generate a string representation of the map with the robot's position.

        Args:
            robot_position (tuple): Coordinates (row, col) of the robot.

        Returns:
            str: String representation of the map with department colours.
        """
        map_copy = [row[:] for row in self.map]
        row, col = robot_position
        map_copy[row][col] = 'R'

        department_colours = {
            'E': '\033[1;37;44m',    # Engineering
            'C': '\033[1;37;46m',    # Command
            'M': '\033[1;37;42m',    # Medical Bay
            'A': '\033[1;37;41m',    # Airlock
            'H': '\033[1;37;43m',    # Hydroponics
            'G': '\033[1;37;47m',    # Cargo
            'D': '\033[1;37m'        # Docking
        }

        map_str = ''
        for row in map_copy:
            for cell in row:
                if cell in department_colours:
                    map_str += department_colours[cell] + cell + '\033[0m    '
                else:
                    map_str += cell + "    "
            map_str += '\n'

        return map_str
