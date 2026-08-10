from math import gcd

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
m = int(input("Enter message (number): "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while gcd(e, phi) != 1:
    e += 1

d = pow(e, -1, phi)

c = pow(m, e, n)
msg = pow(c, d, n)

print("Public Key :", (e, n))
print("Private Key:", (d, n))
print("Encrypted  :", c)
print("Decrypted  :", msg)






#with name

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
text = input("Enter name: ")

from math import gcd

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while gcd(e, phi) != 1:
    e += 1

d = pow(e, -1, phi)

enc = [pow(ord(ch), e, n) for ch in text]
dec = "".join(chr(pow(x, d, n)) for x in enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
