# Local imports
from oblivion import schemes
from oblivion.entities import (
    RSAPublicKey,
    RSAPrivateKey,
)


def test_rsa_encryption_and_decryption_schemes(rsa_keys):
    """Test schemes.rsa_*_scheme_with_oaep_padding."""
    message = b'test'
    label = b'label'
    ciphertext = schemes.rsa_encryption_scheme_with_oaep_padding(
        public_key=rsa_keys[0],
        message=message,
        label=label)
    message2 = schemes.rsa_decryption_scheme_with_oaep_padding(
        private_key=rsa_keys[1],
        ciphertext=ciphertext,
        label=label)
    assert message == message2
