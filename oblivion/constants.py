# Standard imports
from typing import Tuple

# Types
RSAModulus = int
RSAPublicExponent = int
RSAPrivateExponent = int
RSAPublicKey = Tuple[RSAModulus, RSAPublicExponent]
RSAPrivateKey = Tuple[RSAModulus, RSAPrivateExponent]
RSAMsgRepresentative = int
RSACyphertextRepresentative = int
