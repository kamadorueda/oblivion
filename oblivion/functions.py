# Standard imports
import os
import hashlib

# Local imports
from oblivion.constants import (
    HASH_BASE,
    HASH_LENGTH,
)
from oblivion.primitives import (
    integer_to_octet_string_primitive,
)


def hash_func(msg: bytes) -> bytes:
    """Return the digest of msg."""
    return HASH_BASE(msg).digest()


def random_bytes(size: int) -> bytes:
    """Return a safe random octet string."""
    return os.urandom(size)


def mask_generation_function(mgf_seed: bytes, mask_length: int) -> bytes:
    """Mask generation function based on a hash function."""
    # https://tools.ietf.org/html/rfc8017#appendix-B.2.1
    if mask_length > (2 ** 32) * HASH_LENGTH:
        raise ValueError(f'{mask_length} > {(2 ** 32) * HASH_LENGTH}')

    range_length = 1 + mask_length // HASH_LENGTH
    if mask_length % HASH_LENGTH != 0:
        range_length -= 1

    mgf_output = bytes()
    for counter in range(1 + range_length):
        mgf_output += hash_func(
            mgf_seed
            + integer_to_octet_string_primitive(
                length=4,
                integer=counter))
    return mgf_output[:mask_length]
