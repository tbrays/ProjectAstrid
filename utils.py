import os
import random

def clear_console():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def generate_id():
	return random.randint(10, 250)