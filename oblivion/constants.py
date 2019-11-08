# Standard imports
import sys
import hashlib
import textwrap
from typing import Any

# Types
RSAModulus = int
RSAExponent = int
RSAPublicExponent = int
RSAPrivateExponent = int
RSAMsg = bytes
RSALabel = bytes
RSACyphertext = bytes
RSAMsgRepresentative = int
RSACyphertextRepresentative = int

# Crypto constants
HashBase = hashlib.sha3_512
HASH_LENGTH = HashBase().digest_size
MINIMUM_MODULUS_BIT_SIZE = 8 * (2 * HASH_LENGTH + 3)


def get_stack_size():
    size = 2
    while True:
        try:
            # pylint: disable=protected-access
            sys._getframe(size)
            size += 1
        except ValueError:
            return size - 1


def callback(msg: str) -> Any:
    """Callback function to notify progress."""
    print(textwrap.indent(msg, prefix='-' * get_stack_size()), file=sys.stderr)
