class RSAException(Exception):
    """Base exceptions for this package."""


class RSAKeyGenerationException(RSAException):
    """An error ocurred while generating cryptographic keys."""


class RSAEncryptionException(RSAException):
    """An error ocurred while encrypting."""


class RSADecryptionException(RSAException):
    """An error ocurred while decrypting."""
