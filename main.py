from environment import Environment
from robot import Robot


def main():
	luna_9 = Environment()
	astrid = Robot(
		name = "Astrid", 
		manufacturer = "SpaceCorp", 
		model = "RX-101", 
		environment = luna_9
	)
	astrid.start_up()


if __name__ == "__main__":
	main()
