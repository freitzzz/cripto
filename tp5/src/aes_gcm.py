import os
from pathlib import Path
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_aes_gcm(input: bytes, key: bytes, aead: bytes, nonce: bytes):
    return AESGCM(key).encrypt(nonce, input, aead)


def decrypt_aes_gcm(input: bytes, key: bytes, aead: bytes, nonce: bytes):
    return AESGCM(key).decrypt(nonce, input, aead)


def pad(m):
    return m+(chr(16-len(m) % 16)*(16-len(m) % 16)).encode()


block_size = 128
key = os.urandom(int(block_size / 8))
aead = os.urandom(int(block_size / 8))
nonce = os.urandom(12)

input = Path(sys.argv[1]).read_bytes()
cipher_input = encrypt_aes_gcm(pad(input), key, aead, nonce)
output = Path(sys.argv[2]).write_bytes()
