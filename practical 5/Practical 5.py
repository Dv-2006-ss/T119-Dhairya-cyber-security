
# Diffie-Hellman Key Exchange
# Educational implementation

# Public parameters
p = 23   
g = 5    

# Private keys (kept secret)
alice_private = 6
bob_private = 15

# Public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("Alice's public key:", alice_public)
print("Bob's public key:", bob_public)

# Each party calculates the shared secret
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)

print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

# Verify that both calculated the same secret
if alice_shared_secret == bob_shared_secret:
    print("Key exchange successful!")
    print("Shared secret:", alice_shared_secret)
else:
    print("Key exchange failed!")
