# Standard imports
from typing import Tuple


def octet_string_to_integer_primitive(octet_string: bytes) -> Tuple[int, int]:
    """Convert an octet string to a nonnegative integer."""
    # https://tools.ietf.org/html/rfc8017#section-4.2
    nonnegative_integer = \
        sum(value * (256 ** index)
            for index, value in enumerate(reversed(octet_string)))
    return len(octet_string), nonnegative_integer


def integer_to_octet_string_primitive(length: int,
                                      nonnegative_integer: int) -> bytes:
    """Convert a nonnegative integer to an octet string."""
    # https://tools.ietf.org/html/rfc8017#section-4.1
    if nonnegative_integer >= 256 ** length:
        raise ValueError("Integer too large")
    index = 0
    digits = [0] * length
    while nonnegative_integer:
        digits[index] = nonnegative_integer % 256
        nonnegative_integer //= 256
        index += 1
    return bytes(reversed(digits))
