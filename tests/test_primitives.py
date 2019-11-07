# Third parties imports
import pytest

# Local imports
from oblivion import primitives
from oblivion.entities import (
    RSAPublicKey,
    RSAPrivateKey,
)
from oblivion.functions import (
    rsa_generate_keys,
)

# Constants
RSA_PUBLIC_KEY, RSA_PRIVATE_KEY = rsa_generate_keys(256)



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


def test_rsa_encryption_and_decryption_primitive():
    """Test primitives.rsa_*_primitive."""
    message = 123456789
    ciphertext = primitives.rsa_encryption_primitive(RSA_PUBLIC_KEY, message)
    message2 = primitives.rsa_decryption_primitive(RSA_PRIVATE_KEY, ciphertext)
    assert message == message2
