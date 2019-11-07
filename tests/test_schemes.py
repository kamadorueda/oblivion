# Local imports
from oblivion import schemes
from oblivion.entities import (
    RSAPublicKey,
    RSAPrivateKey,
)
from oblivion.functions import (
    rsa_generate_keys,
)

# Constants
RSA_PUBLIC_KEY, RSA_PRIVATE_KEY = rsa_generate_keys(1024)


def test_rsa_encryption_and_decryption_schemes():
    """Test schemes.rsa_*_scheme_with_oaep_padding."""
    message = b'test'
    label = b'label'
    ciphertext = schemes.rsa_encryption_scheme_with_oaep_padding(
        public_key=RSA_PUBLIC_KEY,
        message=message,
        label=label)
    message2 = schemes.rsa_decryption_scheme_with_optimal_asymmetric_encryption_padding(
        private_key=RSA_PRIVATE_KEY,
        ciphertext=ciphertext,
        label=label)
    assert message == message2
