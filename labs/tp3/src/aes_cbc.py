from binascii import hexlify
import os
from pathlib import Path
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_aes_cbc(input: bytes, key: bytes, iv: bytes):
    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    update = encryptor.update(input)
    finish = encryptor.finalize()
    return update + finish


def pad(m):
    return m+(chr(16-len(m) % 16)*(16-len(m) % 16)).encode()


key = os.urandom(16)
iv = os.urandom(16)

Path('input-key').write_bytes(hexlify(key))
Path('input-iv').write_bytes(hexlify(iv))

input = Path(sys.argv[1]).read_bytes()
cipher_input = encrypt_aes_cbc(pad(input), key, iv)
output = Path(sys.argv[2]).write_bytes(cipher_input)
