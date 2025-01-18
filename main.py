"""
This script initialises and runs the humanoid robot simulation.

The program creates an environment and a robot instance, then starts the
robot's operations to perform tasks in the simulated environment.

Classes:
    Environment: Represents the environment the robot operates in.
    Robot: Represents the humanoid robot and its operations.

Functions:
    main(): Initialises the environment and robot, and starts the robot's operations.
"""


from environment import Environment
from robot import Robot


def main():
    """
    Main function to initialise the environment and the robot
    and start the robot's operations.
    """
    # Create the environment
    luna_9 = Environment()

    # Create the robot instance
    astrid = Robot(
        name="Astrid",
        manufacturer="SpaceCorp",
        model="RX-101",
        environment=luna_9
    )

    # Start the robot
    astrid.start_up()


if __name__ == "__main__":
    main()
