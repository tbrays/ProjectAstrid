class Environment:
	def __init__(self):
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
		return self._map

	def is_valid_position(self, row, col):
		return 0 <= row < self.rows and 0 <= col < self.cols and self.map[row][col] != 'X'

	def find_path(self, start_position, destination):
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
		map_copy = [row[:] for row in self.map]
		row, col = robot_position
		map_copy[row][col] = 'R'
		department_colours = {
			'E': '\033[1;37;44m',
			'C': '\033[1;37;46m',
			'M': '\033[1;37;42m',
			'A': '\033[1;37;41m',
			'H': '\033[1;37;43m',
			'G': '\033[1;37;47m',
			'D': '\033[1;37m'
		}

		map_str = ''
		for row in map_copy:
			for cell in row:
				if cell in department_colours:
					map_str += department_colours[cell] + cell + '\033[0m  ' 
				else:
					map_str += cell + "  "
			map_str += '\n'
		return map_str
