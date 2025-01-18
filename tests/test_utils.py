import pytest
from utils import generate_id

def test_generate_id():
		package_id = generate_id()
		assert isinstance(package_id, int)
		assert 10 <= package_id <= 250
