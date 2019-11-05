# Standard imports
import hashlib
from typing import Tuple

# Types
RSAModulus = int
RSAPublicExponent = int
RSAPrivateExponent = int
RSAPublicKey = Tuple[RSAModulus, RSAPublicExponent]
RSAPrivateKey = Tuple[RSAModulus, RSAPrivateExponent]
RSAMsg = bytes
RSALabel = bytes
RSACyphertext = bytes
RSAMsgRepresentative = int
RSACyphertextRepresentative = int

# Crypto constants
HashBase = hashlib.sha3_512
HASH_LENGTH = HashBase().digest_size

#
# Exceptions
#


class RSAException(Exception):
    """Base exceptions for this package."""


class RSAEncryptionException(RSAException):
    """An error ocurred while encrypting."""


class RSADecryptionException(RSAException):
    """An error ocurred while decrypting."""
