# Standard imports
import math
import secrets

# Local imports
from oblivion.constants import (
    HashBase,
    HASH_LENGTH,
)
from oblivion.primitives import (
    integer_to_octet_string_primitive,
)


def hash_func(msg: bytes) -> bytes:
    """Return the digest of msg."""
    return HashBase(msg).digest()


def random_bytes(size: int) -> bytes:
    """Return a safe random octet string."""
    return secrets.token_bytes(size)


def bytes_xor(bytes_a: bytes, bytes_b: bytes) -> bytes:
    """Return the XOR between A and B."""
    if len(bytes_a) != len(bytes_b):
        raise ValueError('Expected equal length octet strings')
    return bytes(a ^ b for a, b in zip(bytes_a, bytes_b))


def jacobi(numerator: int, denominator: int) -> int:
    """Compute the Jacobi Symbol."""
    if denominator <= 0 or denominator & 1 == 0:
        raise ValueError('Jacobi parameters are out of function domain')
    j_symbol: int = 1
    numerator %= denominator
    while numerator:
        while numerator & 1 == 0:
            numerator = numerator // 2
            if denominator % 8 in (3, 5):
                j_symbol *= -1
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            j_symbol *= -1
        numerator %= denominator
    if denominator == 1:
        return j_symbol
    return 0


def is_prime(number, rounds: int = 32) -> bool:
    """Primality test via Solovay-Strassen algorithm."""
    helper: int = (number - 1) // 2
    for _ in range(rounds):
        witness: int = 1 + secrets.randbelow(number - 1)
        if math.gcd(witness, number) != 1:
            return False
        if jacobi(witness, number) % number != pow(witness, helper, number):
            return False
    return True


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
