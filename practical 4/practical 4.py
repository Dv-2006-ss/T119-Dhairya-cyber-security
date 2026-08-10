import hashlib
import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    while True:
        n = random.randint(100, 300)
        if is_prime(n):
            return n

def generate_keys():
    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    d = pow(e, -1, phi)

    return (e, n), (d, n)

def sign_message(message, private_key):
    d, n = private_key

    hash_value = hashlib.sha256(message.encode()).hexdigest()
    hash_number = int(hash_value, 16)

    hash_number = hash_number % n

    signature = pow(hash_number, d, n)

    return signature

def verify_signature(message, signature, public_key):
    e, n = public_key

    hash_value = hashlib.sha256(message.encode()).hexdigest()
    hash_number = int(hash_value, 16)

    hash_number = hash_number % n

    recovered_hash = pow(signature, e, n)

    return recovered_hash == hash_number


print("===== RSA DIGITAL SIGNATURE =====")

public_key, private_key = generate_keys()

print("\nPublic Key:", public_key)
print("Private Key:", private_key)

message = input("\nEnter message: ")

signature = sign_message(message, private_key)

print("\nDigital Signature:", signature)

if verify_signature(message, signature, public_key):
    print("\nSignature Verification: SUCCESS")
    print("Message is authentic and unchanged.")
else:
    print("\nSignature Verification: FAILED")

modified_message = input("\nEnter message again to verify: ")
if verify_signature(modified_message, signature, public_key):
    print("Modified Message Verification: SUCCESS")
else:
    print("Modified Message Verification: FAILED")
    print("Message was changed.")
