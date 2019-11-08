# Standard imports
import math
from typing import Tuple

# Local imports
from oblivion.constants import (
    callback,
)
from oblivion.entities import (
    RSAPublicKey,
    RSAPrivateKey,
)
from oblivion.exceptions import (
    RSAKeyGenerationException,
    RSAEncryptionException,
    RSADecryptionException,
)
from oblivion.functions import (
    generate_hard_to_factor_prime,
    modular_multiplicative_inverse,
)
from oblivion.schemes import (
    rsa_encryption_scheme_with_oaep_padding,
    rsa_decryption_scheme_with_oaep_padding,
)


def test_encryption(public: RSAPublicKey, private: RSAPrivateKey) -> bool:
    """Test cryptographic keys validity by performing a cryptographic round."""
    success: bool = False
    message: bytes = b'm'
    try:
        ciphertext = rsa_encryption_scheme_with_oaep_padding(
            public_key=public,
            message=message)
        message2 = rsa_decryption_scheme_with_oaep_padding(
            private_key=private,
            ciphertext=ciphertext)
    except (RSAEncryptionException, RSADecryptionException):
        success = False
    else:
        success = message == message2
    return success


def rsa_generate_keys(  # noqa: MC0001
        bits: int) -> Tuple[RSAPublicKey, RSAPrivateKey]:
    """Generate public and private keys with (n, d) of the specified bits."""
    public = RSAPublicKey(modulus=0, exponent=0)
    private = RSAPrivateKey(modulus=0, exponent=0)
    reduced_totient_divisor_min_bits: int = bits // 2 ** 4
    while True:
        callback('generating hard to factor prime number "p"')
        # p and q should differ in length by a few digits
        # both (p - 1) and (q - 1) should contain large prime factors
        prime_p = generate_hard_to_factor_prime(bits // 2 - 1)
        callback('generating hard to factor prime number "q"')
        prime_q = generate_hard_to_factor_prime(bits // 2 + 1)
        callback('health check: "p" and "q" differ in a few bits')
        if prime_p.bit_length() == prime_q.bit_length():
            callback('health check failed, retrying')
            continue

        callback('computing modulus "n"')
        public.modulus = prime_p * prime_q
        private.modulus = public.modulus
        # gcd(p - 1, q - 1) should be small
        reduced_totient_divisor: int = math.gcd(prime_p - 1, prime_q - 1)
        if public.modulus_bits >= bits:
            callback(f'health check: "bits on modulus" > "{bits}"')
            if reduced_totient_divisor_min_bits:
                callback('health check: small "gcd(p - 1, q - 1)"')
                if (reduced_totient_divisor.bit_length()
                        < reduced_totient_divisor_min_bits):
                    break
            else:
                break
        callback('health check failed, retrying')
    callback('computing "reduced_totient" of "n"')
    reduced_totient = (prime_p - 1) * (prime_q - 1) // reduced_totient_divisor
    while True:
        callback('generating hard to factor prime number "d"')
        private.exponent = generate_hard_to_factor_prime(bits)
        callback('health check: "d" < "reduced_totient"')
        # It's guaranteed that private.exponent < reduced_totient (FIPS 186-4)
        if private.exponent >= reduced_totient:
            callback('health check failed, retrying')
            continue
        callback('computing public exponent "e"')
        public.exponent = \
            modular_multiplicative_inverse(private.exponent, reduced_totient)
        # Ensure that any message (except for 0 and 1), will be reduced
        #   after performing encryption, this is, M ** e (mod n) will
        #   'wrap around'
        callback('health check: "M ** e (mod n)" must reduce "M ** e"')
        if public.modulus_bits < public.exponent < reduced_totient:
            callback('health check: "gcd(e, reduced_totient) == 1"')
            if math.gcd(public.exponent, reduced_totient) == 1:
                break
        callback('health check failed, retrying')

    callback('health check: "M ** e ** d (mod n) == M"')
    if test_encryption(public, private):
        return public, private
    raise RSAKeyGenerationException('A health check failed, please try again')
