# Third parties imports
import pytest
from typing import Tuple

# Local imports
from oblivion.entities import (
    RSAPublicKey,
    RSAPrivateKey,
)
from oblivion.generate import (
    rsa_generate_keys,
)


@pytest.fixture(scope='session')
def rsa_keys() -> Tuple[RSAPublicKey, RSAPrivateKey]:
    """Fixture a RSA Key."""
    return rsa_generate_keys(1280)
