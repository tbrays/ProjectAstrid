import pytest
import time
from robot import Robot
from environment import Environment
from unittest.mock import patch

@pytest.fixture
def environment():
    return Environment()

@pytest.fixture
def robot(environment):
    return Robot(name="Astrid", model="RX-101", manufacturer="SpaceCorp", environment=environment)

def test_robot_initialisation(robot):
    assert robot.name == "Astrid"
    assert robot.model == "RX-101"
    assert robot.manufacturer == "SpaceCorp"
    assert robot.position == (6, 0)  # Check if the initial position is correct
    assert robot.inventory == []  # Ensure inventory is initially empty

def test_delivery_method(robot, environment, monkeypatch):
    # Mock the find_path method to simulate robot movement
    def mock_find_path(position, destination):
        return [(6, 1), (6, 2)]  # Mocked path

    # Mock input() to prevent it from hanging during testing
    monkeypatch.setattr('builtins.input', lambda x: None)
    
    # Mock time.sleep to avoid delays during testing
    monkeypatch.setattr(time, 'sleep', lambda x: None)

    # Mock the display_delivery_menu to return a valid department name
    monkeypatch.setattr(robot.interface, 'display_delivery_menu', lambda: "Medical Bay")
    
    monkeypatch.setattr(environment, "find_path", mock_find_path)

    robot.delivery()  # Simulate delivery
    assert robot.position == (6, 2)  # Robot should be at the destination
    assert len(robot.inventory) == 0  # Inventory should be cleared after delivery


