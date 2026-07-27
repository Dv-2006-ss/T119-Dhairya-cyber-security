import hmac
import hashlib
import secrets
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

# ---------- HMAC (hash-based MAC) ----------

def generate_hmac(message: bytes):
    key = secrets.token_bytes(32)
    tag = hmac.new(key, message, hashlib.sha256).digest()
    print("Message:", message)
    print("Secret Key:", key.hex())
    print("HMAC:", tag.hex())
    return key, tag

def verify_hmac(key: bytes, message: bytes, tag: bytes) -> bool:
    valid = hmac.compare_digest(hmac.new(key, message, hashlib.sha256).digest(), tag)
    print("HMAC Valid:", valid)
    return valid


# ---------- CMAC (AES block-cipher-based MAC) ----------

def generate_cmac(message: bytes):
    key = secrets.token_bytes(16)  # AES-128 key
    c = cmac.CMAC(algorithms.AES(key))
    c.update(message)
    tag = c.finalize()
    print("Message:", message)
    print("Secret Key:", key.hex())
    print("CMAC:", tag.hex())
    return key, tag

def verify_cmac(key: bytes, message: bytes, tag: bytes) -> bool:
    c = cmac.CMAC(algorithms.AES(key))
    c.update(message)
    try:
        c.verify(tag)
        print("CMAC Valid: True")
        return True
    except Exception:
        print("CMAC Valid: False")
        return False


# ---------- Run: one message, generate then verify ----------

text = input("Enter message: ")
message = text.encode()

print("\n--- HMAC ---")
key1, tag1 = generate_hmac(message)
verify_hmac(key1, message, tag1)

print("\n--- CMAC ---")
key2, tag2 = generate_cmac(message)
verify_cmac(key2, message, tag2)