import pytest
import re
from environment import Environment

@pytest.fixture
def environment():
    return Environment()

def test_environment_initialisation(environment):
    # Test the environment's initial setup
    assert environment is not None  # Environment should be created

def test_find_path(environment):
    # Mock position and destination
    path = environment.find_path((6, 0), "Airlock")
    assert isinstance(path, list)
    assert len(path) > 0  # Ensure a valid path is returned

def remove_color_codes(text):
    """
    Remove ANSI escape sequences (color codes) from a string.
    """
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def test_generate_map(environment):
    map_str = environment.generate_map((6, 0))
    
    # Remove color codes
    clean_map_str = remove_color_codes(map_str)
    
    # Now check if the map is a non-empty string and contains grid-like structure
    assert isinstance(clean_map_str, str)
    assert clean_map_str.strip() != ""  # Ensure map is not empty
    assert any(char in clean_map_str for char in ['X', 'E', 'H', 'R', 'G'])  # Ensure that map contains symbols like 'X', 'E', etc.

