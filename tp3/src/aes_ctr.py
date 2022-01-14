from binascii import hexlify
import os
from pathlib import Path
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_aes_ctr(input: bytes, key: bytes, nonce: bytes):
    encryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
    update = encryptor.update(input)
    finish = encryptor.finalize()
    return update + finish


def pad(m):
    return m+(chr(16-len(m) % 16)*(16-len(m) % 16)).encode()


key = os.urandom(16)
nonce = os.urandom(16)

Path('input-key').write_bytes(hexlify(key))
Path('input-nonce').write_bytes(hexlify(nonce))

input = Path(sys.argv[1]).read_bytes()
cipher_input = encrypt_aes_ctr(pad(input), key, nonce)
output = Path(sys.argv[2]).write_bytes(cipher_input)
