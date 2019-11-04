# Third parties imports
import pytest

# Local imports
from oblivion import primitives


@pytest.mark.parametrize(
    "args,result", [
        (b'test', (4, 1952805748)),
    ])
def test_octet_string_to_integer_primitive(args, result):
    """Test primitives.octet_string_to_integer_primitive."""
    assert primitives.octet_string_to_integer_primitive(args) == result


@pytest.mark.parametrize(
    "args,result", [
        ((4, 1952805748), b'test'),
    ])
def test_integer_to_octet_string_primitive(args, result):
    """Test primitives.integer_to_octet_string_primitive."""
    assert primitives.integer_to_octet_string_primitive(*args) == result
