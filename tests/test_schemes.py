# Local imports
from oblivion import schemes
from oblivion.constants import (
    RSAPublicKey,
    RSAPrivateKey,
)


def test_rsa_encryption_and_decryption_schemes(
        rsa_public_key: RSAPublicKey,
        rsa_private_key: RSAPrivateKey):
    """Test schemes.rsa_*_scheme_with_oaep_padding."""
    message = b'test'
    label = b'label'
    ciphertext = schemes.rsa_encryption_scheme_with_oaep_padding(
        recipient_public_key=rsa_public_key,
        message=message,
        label=label)
    message2 = schemes.rsa_decryption_scheme_with_optimal_asymmetric_encryption_padding(
        recipient_private_key=rsa_private_key,
        ciphertext=ciphertext,
        label=label)
    assert message == message2
