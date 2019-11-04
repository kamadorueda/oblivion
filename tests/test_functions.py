# Third parties imports
import pytest

# Local imports
from oblivion import functions


@pytest.mark.parametrize(
    "args,result", [
        ((b'test', 1), b'\x1b'),
    ])
def test_mask_generation_function(args, result):
    """Test functions.mask_generation_function."""
    assert functions.mask_generation_function(*args) == result
